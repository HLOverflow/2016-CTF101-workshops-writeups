Challenge description:
===
Pssss. I heard that you have a reputation for "helping people to get stuff". Can you help me to get the secret at http://web.spro.ink:3002/secret.php?

Prerequisite skills:
===
Ability to “not follow redirects”

---
When we go to http://web.spro.ink:3002/secret.php, we were redirected to index.php where login is required.

1. Use curl because curl by itself does not follow redirects unless specified -L
    ```sh
	milkyway@ctf101-shell:~$ curl http://web.spro.ink:3002/secret.php
	TOP SECRET: <img src='qr_code.jpg' /
    ```
2. Go to http://web.spro.ink:3002/qr_code.jpg
    ![qrcode](https://github.com/HLOverflow/2016-CTF101-workshops-writeups/blob/master/challenge3/challenge3.jpg "qr code")

3. Scan QR code with [online QR code scanner](https://webqr.com/)
---
flag{wh0_54y5_y0u_n33d_70_f0ll0w_r3d1r3c75?}
