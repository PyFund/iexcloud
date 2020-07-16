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

The package requires active subscription to IEX
Cloud. To learn more about IEX Cloud, visit https://iexcloud.io.

To be able to use iexcloud, there environment variable `IEX_TOKEN`
needs to be configured:

#### Setting your environment variables

```python
import iexcloud

iexcloud.set_token({YOUR_IEX_CLOUD_TOKEN})
```
