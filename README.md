# iexcloud

iexcloud is the python wrapper for [IEX Cloud](https://iexcloud.io) API.

## Installation 

### Getting the package

The source code is currently hosted on GitHub at: 
https://github.com/shawnlinxl/iexcloud

Binary installers for the latest released version are available at the [Python
package index](https://pypi.org/project/iexcloud).

```sh
pip install iexcloud
```

### Dependencies

The package should be used with conjunction with a MySQL database and an IEX
Cloud. To learn more about IEX Cloud, visit https://iexcloud.io.

To be able to use iexcloud, there are several key environment variables that
need to be configured:

* IEX_TOKEN: Your IEX Cloud Api Token
* MYSQL_USER: Your MySQL username
* MYSQL_PASS: Your MySQL password
* MYSQL_HOST: Your MySQL hostname
* MYSQL_PORT: Your MySQL port number

#### Setting your environment variables

1. OS X

   * Open Terminal
   * Run `touch ~/.bash_profile; open ~/.bash_profile`
   * In TextEdit, add

     ```
     export IEX_TOKEN="Your IEX Cloud Api Token"
     export MYSQL_USER="Your MySQL username"
     export MYSQL_PASS="Your MySQL password"
     export MYSQL_HOST="Your MySQL hostname"
     export MYSQL_PORT="Your MySQL port number"
     ```
     
   * Save the .bash_profile file and Quit (Command + Q) Text Edit.
   * Run source `~/.bash_profile`

2. Linux

   * Open Terminal
   * Run `sudo -H vim /etc/environment`
   * Enter password
   * In terminal, press `i` to enter insert mode
   * In terminal, add
   
     ```
     IEX_TOKEN="Your IEX Cloud Api Token"
     MYSQL_USER="Your MySQL username"
     MYSQL_PASS="Your MySQL password"
     MYSQL_HOST="Your MySQL hostname"
     MYSQL_PORT="Your MySQL port number"
     ```  
   * Press `esc` to quit edit mode.
   * Enter `:wq` to save and exit.