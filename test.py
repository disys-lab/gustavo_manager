import requests, json, pickle, redis
KEYGEN_ACC_ID="34b683d0-6121-4a5a-ac92-ee6320611484"
machine_fingerprint="64e5efbb207b61ecc8758f186dd094a29adab4e000011ecc6565d4dd25923040"
license_key="key/eyJob3N0X2lwIjogIjE3Mi4xNy4wLjEiLCAiZXhwaXJlcyI6ICIyMDI2LTAxLTIzVDA2OjM5OjEyLjkzNFoifQ==.fPKh5Tfk6kO4jgFK7DiPPWmSKtPF5jkUv4ztXAy4Zp_1fii5W0jBSlJmHZLxvHqpY74QVa0d5L013TUT8OyFDg=="
validation = requests.post(
                "https://api.keygen.sh/v1/accounts/{}/licenses/actions/validate-key".format(KEYGEN_ACC_ID),
                headers={
                    "Content-Type": "application/vnd.api+json",
                    "Accept": "application/vnd.api+json",
                },
                data=json.dumps(
                    {
                        "meta": {
                            "scope": {"fingerprint": machine_fingerprint},
                            "key": license_key,
                        }
                    }
                ),
            ).json()
print(validation)
validation_record = validation
r = redis.StrictRedis(host="192.168.1.88",port="6379",password="e87052bfcc0b65b2d0603ad4baa8d8ced7aa929b6698a568d2ce53dfd2dc04bcs")
r.set(str(machine_fingerprint)+"_validation_record", pickle.dumps(validation_record), ex=3600 )
