```markdown
# Endless Online Global Chat to Discord Webhook

This script uses Frida to hook into the global chat functionality of the game Endless Online and forwards all chat messages to a Discord webhook.

## Functionality

* **Hooks into `Endless.exe`:** The script attaches to the `Endless.exe` process.
* **Targets specific memory address:** It specifically targets the memory address `Endless.exe+C0885` which is assumed to be responsible for handling chat messages.
* **Reads chat message string:**  When the target address is accessed, the script reads the memory pointed to by a specific offset (`this.context.ebp.add(0x18)`) and attempts to interpret it as a UTF-8 string.
* **Sends message to Discord:** The extracted string, representing the chat message, is then sent to a pre-configured Discord webhook URL.
* **Duplicate message handling:** The script includes a mechanism to prevent sending duplicate messages to the Discord webhook.
* **Error handling:** Basic error handling is implemented to catch issues with reading memory and sending messages to Discord.

## Requirements

* **Python:** The script requires Python to be installed.
* **Frida:** The Frida framework is required for dynamic instrumentation. Install it using `pip install frida`.
* **requests:** The `requests` library is used for sending HTTP requests to the Discord webhook. Install it using `pip install requests`.
* **Discord Webhook:** A Discord webhook URL is required to receive the chat messages.

## Configuration

1. **Discord Webhook URL:** Replace the placeholder `webhook_url` with your actual Discord webhook URL.
2. **Target Process:** The `target_process` variable is set to `Endless.exe`. Ensure this matches the name of the Endless Online executable.
3. **Target Address:** The `target_address` variable is set to `Endless.exe+C0885`. This might need to be adjusted based on the specific version of Endless Online.

## Usage

1. Save the script as a Python file (e.g., `eo_chat_to_discord.py`).
2. Run the script: `python eo_chat_to_discord.py`
3. Launch Endless Online.

## Disclaimer

This script is provided for educational purposes only. Use it responsibly and be aware of the terms of service of both Endless Online and Discord. Modifying game behavior might be against the game's rules.

## Future Improvements

* **Dynamic address resolution:** Implement a more robust method to dynamically determine the target address instead of hardcoding it.
* **Configuration file:** Use a configuration file to store the webhook URL and other settings.
* **GUI:** Develop a graphical user interface for easier configuration and monitoring.
```
