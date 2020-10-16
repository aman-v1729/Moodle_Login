# Automated Moodle Login

This is an automated tool which can be used to login to Moodle and navigate to course pages for Mac users.
Login is as easy as typing moodle in the terminal and letting the script do its magic.
It also accepts auto-accepts certificates and can be used to bypass VPL errors.

**Opens a separate instance of chrome with a temporary user for security reasons.**


# Setup
Need to install:
- [chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/): A web driver for  Google Chrome. 
- Clone the repository and copy the **moodle** executable.
	The executable can also be downloaded directly from [here](https://drive.google.com/drive/folders/1WtUfB2V3KpmspoVpKSMV-rRrzxhDeKx1?usp=sharing): 

Move both files to **/usr/local/bin** using the terminal:
```bash
mv path/to/executable /usr/local/bin
```

Give executable rights to the script using the terminal:
```bash
chmod 755 /usr/local/bin/moodle
```

Setup complete!

# Usage
In the terminal, enter:
```bash
moodle
```
You will be prompted to enter your credentials and will be redirected to Moodle. The script may take 15-20 seconds to execute.

## Advanced
- Navigating to course page:

	```bash
	moodle col106
	```
	Navigates to COL106 course page
- Opening VPL:
	```bash 
	moodle vpl
	```
	Redirects to COL106 course page. No certificates need to be accepted.
	| :warning: Warning: Security|
	|:---------------------------|
	| Do not browse on the chrome instance created after using ***vpl*** argument. 		Only use it for programming on VPL as it may accept unverified certificates across the web. |
>**Note**: Separate instance with no user data is created so no risk of privacy invasion.

- **Storing credentials:** by storing your kerberos id and password as environment variables on your local user, running the script would not require you to enter the username and password again and again. 
	To do this, set environment variables KERBEROS_ID and KERBEROS_PASS
	in ~/.bash_profile
	```bash
	echo export KERBEROS_ID="cs5190419" >> ~/.bash_profile
	echo export KERBEROS_PASS="your_password" >> ~/.bash_profile
	```



# Development
If running the executable there are no other prerequisites, however for running the python script you would have to set up python and then use:
```bash
pip install -r requirements.txt
python3 launch_moodle.py
```

# License
Licensed under the [MIT License](LICENSE)
