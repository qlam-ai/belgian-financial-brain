# belgian-financial-brain
LLM fuelled by data about the Belgian Stock Market


How to automate the data retrieval process (on Mac OS)
Yes, you can schedule a Python script to run daily at 8 am on your MacBook Pro using **cron**, a Unix-based scheduler available on macOS.

Here's a step-by-step guide:

### 1. Find the Path to Your Python Script
Make sure you know the absolute path to your Python script. For example, if it's in your home directory, it might look like:
```plaintext
/Users/yourusername/path/to/your_script.py
```

### 2. Find the Path to Your Python Interpreter
To make sure you use the correct Python version, locate the path to the Python interpreter you want to use. You can find it by running this command in Terminal:
```bash
which python3
```
This command will give you a path like `/usr/local/bin/python3` or similar. Use this exact path in your cron job.

### 3. Edit Your Cron Jobs
To create or edit cron jobs, open the crontab (cron table) file in your terminal:
```bash
crontab -e
```

### 4. Add a New Cron Job
Once inside the crontab editor, add a new line to schedule your Python script. To run it every day at 8 am, use this line:
```plaintext
0 8 * * * /usr/local/bin/python3 /Users/yourusername/path/to/your_script.py
```

**Explanation of the cron syntax:**
- `0 8 * * *` - This specifies the time to run the job:
  - `0` (minute) means "at minute 0"
  - `8` (hour) means "at 8 am"
  - `* * *` (day, month, and weekday) means "every day, every month, regardless of weekday."
- `/usr/local/bin/python3` is the path to the Python interpreter.
- `/Users/yourusername/path/to/your_script.py` is the path to your script.

### 5. Save and Exit
After adding the line, save and exit. In the `nano` editor (often used for `crontab -e`), press `Ctrl + X`, then `Y` to confirm, and `Enter` to save.

### 6. Verify the Cron Job
To verify that the job was saved correctly, you can list all cron jobs with:
```bash
crontab -l
```

### 7. Check the Output (Optional)
By default, cron jobs do not show output. If you want to log the output or errors to a file for debugging, modify the cron job like this:
```plaintext
0 8 * * * /usr/local/bin/python3 /Users/yourusername/path/to/your_script.py >> /Users/yourusername/path/to/logfile.log 2>&1
```

This will log any output or errors to `logfile.log` for review.

After following these steps, your Python script will automatically run every day at 8 am!