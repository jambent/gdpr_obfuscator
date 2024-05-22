## Obfuskator: Obfuscate CSV file data within Amazon S3
**Obfuskator** provides a simple way to obfuscate specific fields within CSV files that are stored in the Amazon S3 service.
Designed to be used within Amazon Lambda, EC2 and ECS services, **Obfuskator** returns a bytes object of the obfuscated file data that
can be easily processed by, for example, the boto3 S3.Client.put_object function.


## Setup
Install the latest version of obfuskator with:
```
pip install obfuskator
```