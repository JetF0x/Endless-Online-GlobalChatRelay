import frida
import sys
import requests

# Your Discord webhook URL
webhook_url = "REPLACE_ME"

target_process = "Endless.exe"
target_address = "Endless.exe+C0885"

script_code = """
Interceptor.attach(Module.getBaseAddress('Endless.exe').add(0xC0885), {
    onEnter: function(args) {
        var value = this.context.ebp.add(0x18).readPointer();
        console.log('Value being moved to ECX:', value);

        try {
            var strValue = value.readUtf8String();
            console.log('String at ECX:', strValue);
            send(strValue)
        } catch (e) {
            console.log('Failed to read memory as string:', e.message);
        }
    }
});
"""

# Variable to store the last sent message
last_sent_message = None

def send_to_discord(message):
    global last_sent_message

    if message == last_sent_message:
        print(f"Duplicate message detected: {message}")
        return

    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print(f"Failed to send message to Discord: {response.status_code}, {response.text}")
    else:
        # Update last sent message
        last_sent_message = message

def on_message(message, data):
    if message['type'] == 'send':
        log_message = "[*] {0}".format(message['payload'])
        print(log_message)
        send_to_discord(log_message)
    else:
        print(message)
        send_to_discord(str(message))

def main():
    session = frida.attach(target_process)
    script = session.create_script(script_code)
    script.on('message', on_message)
    script.load()
    sys.stdin.read()

if __name__ == "__main__":
    main()
