#Note works only on windows
import subprocess

def text_to_speech(text):
#defining the script
    script=f'''Add-Type -AssemblyName "System.Speech"
                $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
                $synth.Speak("{text}")
                '''
    #running the powershell(cmd) script using subprocess
    process=subprocess.Popen(["powershell","-Command",script],stdout=subprocess.PIPE)
    stdout,stderr=process.communicate()
    
    # Handle any errors
    if stderr:
        print(f"Error: {stderr.decode()}")
    else:
        print("Text-to-speech conversion successful!")
        

if __name__=="__main__":
    print("Welcome to Text to Speech Convertor for dumb people")
    while True:
        x =input("Enter what to pronounce :")
        if x=="q":
            text_to_speech("You are dumb person. Bye Bye ")   
            break 
        
        text_to_speech(x)
            


    
'''Explanation:
script:
This string contains the PowerShell commands to load the necessary assembly and convert the given text into speech.

subprocess.Popen:
This function is used to invoke the PowerShell command. We pass the command powershell and the script as arguments.
stdout=subprocess.PIPE captures the output from the PowerShell process (if any).
stderr=subprocess.PIPE captures any error messages.

process.communicate():
This waits for the PowerShell process to complete and retrieves the output or errors.

Error Handling:
If PowerShell encounters an issue, you can handle it by checking stderr and printing any error messages.

How It Works:
When you run the Python program, it asks you to input text.
The program then sends the input text to the PowerShell script for speech conversion.
The PowerShell script reads the text aloud using the SpeechSynthesizer.
'''

    
    