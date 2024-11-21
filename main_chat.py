import pandas as pd
import json
from fuzzywuzzy import process
from mlx_lm import load, generate
import re
import functools
import threading
import time
import sys


company_names = {
    "ucb": "UCB.BR",
    "abinbev": "ABI.BR",
    "aedifica": "AED.BR",
    "ageas": "AGS.BR",
    "aperam": "APAM.AS",
    "argenx": "ARGX.BR",
    "belgian national bank": "BNB.BR",
    "cofinimmo": "COFB.BR",
    "elia": "ELI.BR",
    "ishares msci belgium etf": "EWK",
    "groupe bruxelles lambert sa": "GBLB.BR",
    "galapagos nv": "GLPG.AS",
    "kbc bank": "KBC.BR",
    "melexis nv": "MELE.BR",
    "proximus": "PROX.BR",
    "sofina": "SOF.BR",
    "solvay": "SOLB.BR",
    "umicore": "UMI.BR",
    "unified post group": "UPG.BR",
    "warehouses de pauw": "WDP.BR",
    "xior student housing": "XIOR.BR",
}

companies = list(company_names.keys())
# Threshold for acceptable similarity (0-100 scale)
threshold = 80
model, tokenizer = load("mlx-community/Llama-3.2-3B-Instruct-4bit")


def find_best_match(user_input, company_list, threshold):
    # Find the best match with score
    best_match, best_score = process.extractOne(user_input, company_list)

    # Check if the best match meets the threshold
    if best_score >= threshold:
        return best_match
    else:
        return "none"


def read_file_to_string(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Error: File not found."
    except IOError:
        return "Error: Could not read the file."


def retrieve_stock_etf_info(companies: list, stock_name: str, threshold: int) -> str:
    stock_name = stock_name.lower()
    result = find_best_match(stock_name, companies, threshold)
    # let's do a fuzzy match with the company names and retrieve the most relevant company name
    res = ""
    if result != "none":
        file_content = read_file_to_string("data/" + company_names[result] + ".txt")
        res = json.dumps({"information we have on stock/etf": file_content})
    else:
        res = json.dumps({"error": "transaction id not found."})
    return res


def extract_json(input):

    json_match = re.search(r"\{.*\}", input)
    if json_match:
        json_string = json_match.group()
        data = json.loads(json_string)
        return data
    else:
        return None


def tool_call(message, model, tokenizer):
    message = [
        {
            "role": "user",
            "content": message,
        }
    ]

    # Define tools available for the model to use:
    tool_message = [
        {
            "name": "retrieve_stock_etf_info",
            "description": "get info about a certain stock or etf given the name of the instrument",
            "parameter_definitions": {
                "stock_name": {
                    "description": "Name of the stock or ETF for which we need information",
                    "type": "str",
                    "required": True,
                }
            },
        },
        {
            "name": "directly_answer",
            "description": "Calls a standard (un-augmented) AI chatbot to generate a response given the conversation history",
            "parameter_definitions": {},
        },
    ]
    formatted_input = tokenizer.apply_chat_template(
        message, tools=tool_message, tokenize=False, add_generation_prompt=True
    )
    response = generate(model, tokenizer, prompt=formatted_input, verbose=False)
    json = extract_json(response)
    if json is None or json["name"] == "directly_answer":
        return None
    else:
        names_to_functions = {
            "retrieve_stock_etf_info": functools.partial(
                retrieve_stock_etf_info, companies=companies, threshold=80
            ),
        }

        # to be called after the tool answer
        function_name = json["name"]
        function_params = json["parameters"]
        function_result = names_to_functions[function_name](**function_params)
        return function_result


def message_call(message, tool_response, model, tokenizer):
    if tool_response is not None:
        text = (
            "answer the following question using the given information. Question : '"
            + message
            + "'. Information : '"
            + tool_response
            + "'."
        )
        messages = [
            {
                "role": "user",
                "content": text,
            }
        ]
    else:
        messages = [
            {
                "role": "user",
                "content": message,
            }
        ]
    formatted_input = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

    response = generate(model, tokenizer, prompt=formatted_input, verbose=False)
    return response


# Function to display a spinner
def spinner_animation(message="Processing..."):
    spinner_chars = "|/-\\"
    idx = 0
    while not stop_spinner_event.is_set():
        sys.stdout.write(f"\r{message} {spinner_chars[idx]}")
        sys.stdout.flush()
        idx = (idx + 1) % len(spinner_chars)
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * (len(message) + 4) + "\r")  # Clear the line


def chat_mode():
    print("Welcome to the Chat Interface! Type 'exit' to end the session.\n")

    # Initialize history
    chat_history = []

    while True:
        try:
            # Step 1: Get input from the user
            user_input = input("You: ")

            # Step 2: Exit condition
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            # Step 3: Combine chat history with the new input
            context = "\n".join(chat_history + [f"You: {user_input}"])

            # Step 4: Start spinner in a separate thread
            global stop_spinner_event
            stop_spinner_event = threading.Event()
            spinner_thread = threading.Thread(target=spinner_animation)
            spinner_thread.start()

            # Step 5: Process the input using tool_call and message_call
            tool_answer = tool_call(context, model, tokenizer)
            final_answer = message_call(context, tool_answer, model, tokenizer)

            # Step 6: Stop the spinner
            stop_spinner_event.set()
            spinner_thread.join()

            # Step 7: Add to chat history
            chat_history.append(f"You: {user_input}")
            chat_history.append(f"Assistant: {final_answer}")

            # Step 8: Display the response to the user
            print(f"Assistant: {final_answer}")

        except Exception as e:
            # Stop the spinner in case of an error
            stop_spinner_event.set()
            spinner_thread.join()
            # Handle unexpected errors gracefully
            print(f"Assistant: Sorry, something went wrong. ({str(e)})")


# Run the chat mode
if __name__ == "__main__":
    chat_mode()
