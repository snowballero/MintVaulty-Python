<p align="center">
  <br>
  <img src="mintvaulty.png" alt="MintVaulty" width="300">
  <br>
  <h1 align="center">MintVaulty</h1>
  <div align="center">
      <span style="font-size:22px;">Strong passwords. No sugarcoating.</span>
  </div>
  <br><br>
  <div align="center">
    <a href="https://github.com/snowballero/MintVaulty-Python/releases/">Install</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#usage">Usage</a>
    <a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;</a>
    <a href="https://github.com/snowballero/MintVaulty-Python/blob/main/LICENSE">License</a>
  </div>
</p>

<h1>What is MintVaulty?</h1>
MintVaulty is a cryptographically secure password generator. It runs offline, has no telemetry and doesn't steal any personal information. I designed it to be open-source, so that everyone can view the code.<br>
Worth noticing: For now , the passwords are stored in plain .txt , this will improve later on.

<h1 id="Install">Installation</h1>
1. Clone the repo
```bash
git clone https://github.com/snowballero/mintvaulty-python

2. Change directory to it
cd mintvaulty-python

3. Execute the file
<br>
    [*] Windows

    ```bash
    python mintvaulty.py
    ```
    
    [*] Linux / macOS

    ```bash
    python3 mintvaulty.py
    ```

3.1 Or all in one command..?
    Linux / macOS
    
    ```bash
    git clone https://github.com/snowballero/mintvaulty-python && cd mintvaulty-python && python3 mintvaulty.py
    ```
    
    Windows
    ```bash
    git clone https://github.com/snowballero/mintvaulty-python; cd mintvaulty-python; python mintvaulty.py
    ```

<h1 id="usage">Usage</h1>

Generate a password:
<h3>Amount of letters: [input, e.g 8]</h3>
<h3>Amount of numbers: [input, e.g 4]</h3>
<h3>Amount of symbols: [input, e.g 2]</h3>
<h3>The program will then ask you to save, which you can reply with y(Y) to continue saving, or n(N) to exit.</h3>

<h2>EXAMPLE:</h2>
<br>
<img src=usage.png>
<br>
After saving the file , it will be located in your current directory.
