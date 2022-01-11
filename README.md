# XResponse

XResponse is a very simple package that has some reusable responses for DRF to be used throughout the apis built at xKern.

###### Usage

* Install the package
  
  ```
  pip install git+https://github.com/xKern/xresponse.git
  ```

* Add the following line to your settings.py module

```
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'xresponse.exception_handler'
}
```


