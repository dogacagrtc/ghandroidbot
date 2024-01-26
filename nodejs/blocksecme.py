import requests
def blocksecme():


    url = "https://firehose.us-east-1.amazonaws.com/"

    payload = "{\"DeliveryStreamName\":\"jackalope-prod-firehose\",\"Records\":[{\"Data\":\"eyJhY2N1cmFjeSI6MC4wLCJhY3Rpdml0eUNvbmZpZGVuY2UiOjAsImFjdGl2aXR5VHlwZSI6IlVua25vd24iLCJhbHRpdHVkZSI6MC4wLCJhcHBfdmVyc2lvbiI6IjQuNTUuMSIsImJlYXJpbmciOjAuMCwiYnJhemVFdmVudCI6ZmFsc2UsImNhcnJpZXIiOiJULU1vYmlsZSIsImNvdXJpZXJJZCI6ImVmN2E5ZjdkLTg1ZjEtNGI0NS1hMjg0LTM5YmIzZjQ4YTE4MCIsImN1cnJlbnRDaGFyZ2UiOjEwMCwiZGV2aWNlTWFudWZhY3R1cmVyIjoiR29vZ2xlIiwiZGV2aWNlTW9kZWwiOiJzZGtfZ3Bob25lNjRfYXJtNjQiLCJkZXZpY2VfaWQiOiI3YjRiMTViYi02MWFlLTQ5NjAtOTJjZi0wMjNkYWY1M2E2ZDQiLCJkcml2ZXJJZCI6ImVmN2E5ZjdkLTg1ZjEtNGI0NS1hMjg0LTM5YmIzZjQ4YTE4MCIsImV2ZW50Q2F0ZWdvcnkiOiJzY2hlZHVsaW5nIiwiZXZlbnRMYWJlbCI6ImFkZF9ibG9ja190YXAiLCJpc0NoYXJnaW5nIjpmYWxzZSwiaXNGcm9tTW9ja0xvY2F0aW9uUHJvdmlkZXIiOmZhbHNlLCJpc0luRm9yZWdyb3VuZCI6dHJ1ZSwiaXNOZW9uIjp0cnVlLCJsYXRMbmciOiJOQSIsImxhdGl0dWRlIjowLjAsImxvbmdpdHVkZSI6MC4wLCJtZXNzYWdlIjoiVzZFa05aaXdQNi1CSU5RNTlDaFNhdyIsIm5vdGlmaWNhdGlvbkNhdGVnb3J5IjoiTi9BIiwibm90aWZpY2F0aW9uSWQiOiJOQSIsIm9yZGVySWQiOiJOQSIsIm9zIjoiMjIyIiwicGhvbmVUeXBlIjoiQW5kcm9pZCwgMzMiLCJwbGF0Zm9ybSI6IkFuZHJvaWQiLCJyZWdpb25JZCI6IjQ2ODZkNDJlLWI5YmQtNGJjMC1hODg3LWM1ZThmYjc4ZTJiZSIsInJlcXVlc3QiOiJOQSIsInNwZWVkIjowLjAsInRpbWVTZW50IjoiTi9BIiwidGltZXN0YW1wIjoiMjAyMzAzMDZUMjMwNjM3LjQ3NFoiLCJ0cmlwSWQiOiJOQSIsIndheXBvaW50SWQiOiJOQSJ9Cg==\"}]}"
    headers = {
        "x-newrelic-id": "VQQDVlBVGwEFUVZRBAMBVQ==",
        "authorization": "AWS4-HMAC-SHA256 Credential=ASIAVEHGYS4FH5U3NA45/20230307/us-east-1/firehose/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token;x-amz-target, Signature=a2d585400ed7ea052da171be1140293d798c55d49283f83c902e7e1a6a365ad3",
        "x-amz-date": "20230307T171006Z",
        "aws-sdk-invocation-id": "52ae1c43-e2e2-40a3-a68b-d80ef204f705",
        "content-encoding": "gzip",
        "user-agent": "aws-sdk-android/2.16.8 Linux/5.15.41-android13-8-00205-gf1bf82c3dacd-ab8747247 Dalvik/2.1.0/0 en_US com.amazonaws.mobileconnectors.kinesis.kinesisrecorder.KinesisFirehoseRecorder/2.16.8",
        "aws-sdk-retry": "0/0",
        "accept-encoding": "identity",
        "x-amz-security-token": "IQoJb3JpZ2luX2VjEHoaCXVzLWVhc3QtMSJGMEQCIGjx+BlZrGnY0m1QTpzxQTA7YjEat7+qu5oq8FDxyB8mAiBHzm1PjsD0EShQb9OsmPyDrJ8oNxpSgxnkaimqDDDkgyqSBggyEAYaDDM1MjY3MTI3NDc2MiIM2okl0AGZvuQDSWfRKu8F8teE7HG8b7fxyhM5I7n3mwHMHl1FGuxAfBK8KrG5zp1DW9TfmWfFmeiHPcQa+MmymLxYDuc/Aig/A637hwMj4Iay/Wm8hi/+HEu2C9Sx9O8B5TDnQ82c542B5zD3avaMiAzB3BLT+Gcjt5TnYQRMvzA/Jv0dB/YklSkU9RiHhPzJSJEa9oGbuBEhzGoV2QjIHB90mrByxq6AicufZzLLN1iLJLgiEt3yMjHZvNt2BxSI1yjeiV2OE+XJMx1GPEE/MZKUhA9UKBZlacbcMqTX2SMe1RfH7cNy6ptWzKVwV8Tlt5nS70299mXJskGNxLwwQjbu1s68gpmQIEoqR7YKBZKNjq9n66xDDKb03GY/wANLz2REjYIzi5n86WMn6CDGcwdfiaB10FvDQawLUQsU/9lyZ089477Tmu2mosA/SDgcWNR1Q665w28xzeDt+Iem+MQqOAwpdfh0qL8ioEb5Q2EYHjDuXKi87IdMpQa4tzGRmpsfoqQrMQwZ69KJ4j8/HfqkBezdWxZ4+FRhLiMe8Kyceiuziuk6Q/TXElM39M421NqWjbcv+7c470YgQ2mY8YCOijve7OPundPCs83RgYRnN5YyVZYB5cFo4pZNc5PbVj1BUpLtc1WmKyt1CIAb7RbZZkkSYwVXvv3o9fH1XFfidKYb2jAFHB5zg2DgF1SZJUM6Tc7/QqiApOxnYMHQQjqd+7nU3Ku5g97CIBrNc557C7a8gnkvdX/yrZsASQiIPCPqK/FT4/pb2dWUohJZPJgV9xyMgrUoSfNa9oozOpnuFg7Ep2IogTnQwEYPBSEvWgbftiUnHqO9kE9miu6VvDQ7KwfcE8tbM13iGpv2bIiCKLo9QGZIIt1hmKdACOObueUKAd9xIi4wZ++/O1DMf07pf1iFAUA7CBTM/W4SeCZn8Sveb7/mrImCAZJoELq4igLDR/NBnFv8cMWhIGqpqrMv/FPaylOXu/LZe5fzYwmKKyIUzfVH19vXQKk65jD73Z2gBjqIArO19FQL4TkhdyU4N49Q9iObNQWFFhL5CoiaGMvYxDR+WtJWOdI2fhCzZIYtrnohusc8IZELjZzFTclV9YqBpArHghkc4UwjJiHdu38cepbLxcJ+Sagj7IihnpZl/FSCQxHuNsSjxRqW0Q01Kt5P8PNxDWYmZvx7HJfGpOXlxwiUPjkXbA4UCKhpe5ZWAbjgxsMCCJzDQ4sf++PyFFsNsQqVdVbA5DFM8btc7uY7z7fFDcQcFVke8YoJ/F8F/Tiy8qS73fTM+lYMmJcfugPNssnJ6kQC6bfxOd8UAx/8HpeIRHACkycIgWU7JfMsEmTSZNdBtT6yEU5K7HPmw718VUBXmyz8D8wuAA==",
        "x-amz-target": "Firehose_20150804.PutRecordBatch",
        "content-type": "application/x-amz-json-1.1",
        "host": "firehose.us-east-1.amazonaws.com",
        "connection": "Keep-Alive"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)







    url = "https://api-managed-delivery-gtm.grubhub.com/deliverymobilegateway/sws/v1/blocks/open/W6EkNZiwP6-BINQ59ChSaw/pickup"

    querystring = { "includeRemoved": "true" }

    payload = "{\"id\":\"W6EkNZiwP6-BINQ59ChSaw\"}"
    headers = {
        "authorization": "Bearer d5f43c6f-f42d-418e-86d0-32f907aa2b55",
        "x-device-id": "23ea718165dc42e1",
        "accept": "application/json",
        "user-agent": "GHDriver/4.55.1 (Android 13/API: 33)",
        "tracestate": "@nr=0-2-124766-255733263-6389873d743948bc----1678143917305",
        "traceparent": "00-e136616eca204fc899b1c64f8cc6d850-6389873d743948bc-00",
        "newrelic": "eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjEyNDc2NiIsImQuYXAiOiIyNTU3MzMyNjMiLCJkLnRyIjoiZTEzNjYxNmVjYTIwNGZjODk5YjFjNjRmOGNjNmQ4NTAiLCJkLmlkIjoiNjM4OTg3M2Q3NDM5NDhiYyIsImQudGkiOjE2NzgxNDM5MTczMDV9fQ==",
        "content-type": "application/json; charset=utf-8",
        "host": "api-managed-delivery-gtm.grubhub.com",
        "connection": "Keep-Alive",
        "accept-encoding": "gzip",
        "x-newrelic-id": "VQQDVlBVGwEFUVZRBAMBVQ=="
    }

    response = requests.post(url, data=payload, headers=headers, params=querystring)

    print(response.text)


    url = "https://firehose.us-east-1.amazonaws.com/"

    payload = "{\"DeliveryStreamName\":\"jackalope-prod-firehose\",\"Records\":[{\"Data\":\"eyJhY2N1cmFjeSI6MC4wLCJhY3Rpdml0eUNvbmZpZGVuY2UiOjAsImFjdGl2aXR5VHlwZSI6IlVua25vd24iLCJhbHRpdHVkZSI6MC4wLCJhcHBfdmVyc2lvbiI6IjQuNTUuMSIsImJlYXJpbmciOjAuMCwiYnJhemVFdmVudCI6dHJ1ZSwiY2FycmllciI6IlQtTW9iaWxlIiwiY291cmllcklkIjoiZWY3YTlmN2QtODVmMS00YjQ1LWEyODQtMzliYjNmNDhhMTgwIiwiY3VycmVudENoYXJnZSI6MTAwLCJkZXZpY2VNYW51ZmFjdHVyZXIiOiJHb29nbGUiLCJkZXZpY2VNb2RlbCI6InNka19ncGhvbmU2NF9hcm02NCIsImRldmljZV9pZCI6IjdiNGIxNWJiLTYxYWUtNDk2MC05MmNmLTAyM2RhZjUzYTZkNCIsImRyaXZlcklkIjoiZWY3YTlmN2QtODVmMS00YjQ1LWEyODQtMzliYjNmNDhhMTgwIiwiZXZlbnRDYXRlZ29yeSI6InNjaGVkdWxpbmciLCJldmVudExhYmVsIjoiYWRkX2Jsb2NrX3N1Y2Nlc3MiLCJpc0NoYXJnaW5nIjpmYWxzZSwiaXNGcm9tTW9ja0xvY2F0aW9uUHJvdmlkZXIiOmZhbHNlLCJpc0luRm9yZWdyb3VuZCI6dHJ1ZSwiaXNOZW9uIjp0cnVlLCJsYXRMbmciOiJOQSIsImxhdGl0dWRlIjowLjAsImxvbmdpdHVkZSI6MC4wLCJtZXNzYWdlIjoiVzZFa05aaXdQNi1CSU5RNTlDaFNhdyIsIm5vdGlmaWNhdGlvbkNhdGVnb3J5IjoiTi9BIiwibm90aWZpY2F0aW9uSWQiOiJOQSIsIm9yZGVySWQiOiJOQSIsIm9zIjoiMjIyIiwicGhvbmVUeXBlIjoiQW5kcm9pZCwgMzMiLCJwbGF0Zm9ybSI6IkFuZHJvaWQiLCJyZWdpb25JZCI6IjQ2ODZkNDJlLWI5YmQtNGJjMC1hODg3LWM1ZThmYjc4ZTJiZSIsInJlcXVlc3QiOiJOQSIsInNwZWVkIjowLjAsInRpbWVTZW50IjoiTi9BIiwidGltZXN0YW1wIjoiMjAyMzAzMDZUMjMxMTQ2LjE3OFoiLCJ0cmlwSWQiOiJOQSIsIndheXBvaW50SWQiOiJOQSJ9Cg==\"},{\"Data\":\"eyJhY2N1cmFjeSI6MC4wLCJhY3Rpdml0eUNvbmZpZGVuY2UiOjAsImFjdGl2aXR5VHlwZSI6IlVua25vd24iLCJhbHRpdHVkZSI6MC4wLCJhcHBfdmVyc2lvbiI6IjQuNTUuMSIsImJlYXJpbmciOjAuMCwiYnJhemVFdmVudCI6ZmFsc2UsImNhcnJpZXIiOiJULU1vYmlsZSIsImNvdXJpZXJJZCI6ImVmN2E5ZjdkLTg1ZjEtNGI0NS1hMjg0LTM5YmIzZjQ4YTE4MCIsImN1cnJlbnRDaGFyZ2UiOjEwMCwiZGV2aWNlTWFudWZhY3R1cmVyIjoiR29vZ2xlIiwiZGV2aWNlTW9kZWwiOiJzZGtfZ3Bob25lNjRfYXJtNjQiLCJkZXZpY2VfaWQiOiI3YjRiMTViYi02MWFlLTQ5NjAtOTJjZi0wMjNkYWY1M2E2ZDQiLCJkcml2ZXJJZCI6ImVmN2E5ZjdkLTg1ZjEtNGI0NS1hMjg0LTM5YmIzZjQ4YTE4MCIsImV2ZW50Q2F0ZWdvcnkiOiJzY2hlZHVsaW5nIiwiZXZlbnRMYWJlbCI6ImFkZF9ibG9ja19yZXF1ZXN0X2NvbXBsZXRlX29uX3NjcmVlbiIsImlzQ2hhcmdpbmciOmZhbHNlLCJpc0Zyb21Nb2NrTG9jYXRpb25Qcm92aWRlciI6ZmFsc2UsImlzSW5Gb3JlZ3JvdW5kIjp0cnVlLCJpc05lb24iOnRydWUsImxhdExuZyI6Ik5BIiwibGF0aXR1ZGUiOjAuMCwibG9uZ2l0dWRlIjowLjAsIm1lc3NhZ2UiOiJXNkVrTlppd1A2LUJJTlE1OUNoU2F3Iiwibm90aWZpY2F0aW9uQ2F0ZWdvcnkiOiJOL0EiLCJub3RpZmljYXRpb25JZCI6Ik5BIiwib3JkZXJJZCI6Ik5BIiwib3MiOiIyMjIiLCJwaG9uZVR5cGUiOiJBbmRyb2lkLCAzMyIsInBsYXRmb3JtIjoiQW5kcm9pZCIsInJlZ2lvbklkIjoiNDY4NmQ0MmUtYjliZC00YmMwLWE4ODctYzVlOGZiNzhlMmJlIiwicmVxdWVzdCI6Ik5BIiwic3BlZWQiOjAuMCwidGltZVNlbnQiOiJOL0EiLCJ0aW1lc3RhbXAiOiIyMDIzMDMwNlQyMzExNDYuMTc4WiIsInRyaXBJZCI6Ik5BIiwid2F5cG9pbnRJZCI6Ik5BIn0K\"}]}"
    headers = {
        "x-newrelic-id": "VQQDVlBVGwEFUVZRBAMBVQ==",
        "authorization": "AWS4-HMAC-SHA256 Credential=ASIAVEHGYS4FH5U3NA45/20230307/us-east-1/firehose/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token;x-amz-target, Signature=9e376111ec799465163325a7a7878c376c507a41157e5d8b68d96d5831457d25",
        "x-amz-date": "20230307T171515Z",
        "aws-sdk-invocation-id": "eff81bd1-5c1f-4b34-8032-bf454d6fdede",
        "content-encoding": "gzip",
        "user-agent": "aws-sdk-android/2.16.8 Linux/5.15.41-android13-8-00205-gf1bf82c3dacd-ab8747247 Dalvik/2.1.0/0 en_US com.amazonaws.mobileconnectors.kinesis.kinesisrecorder.KinesisFirehoseRecorder/2.16.8",
        "aws-sdk-retry": "0/0",
        "accept-encoding": "identity",
        "x-amz-security-token": "IQoJb3JpZ2luX2VjEHoaCXVzLWVhc3QtMSJGMEQCIGjx+BlZrGnY0m1QTpzxQTA7YjEat7+qu5oq8FDxyB8mAiBHzm1PjsD0EShQb9OsmPyDrJ8oNxpSgxnkaimqDDDkgyqSBggyEAYaDDM1MjY3MTI3NDc2MiIM2okl0AGZvuQDSWfRKu8F8teE7HG8b7fxyhM5I7n3mwHMHl1FGuxAfBK8KrG5zp1DW9TfmWfFmeiHPcQa+MmymLxYDuc/Aig/A637hwMj4Iay/Wm8hi/+HEu2C9Sx9O8B5TDnQ82c542B5zD3avaMiAzB3BLT+Gcjt5TnYQRMvzA/Jv0dB/YklSkU9RiHhPzJSJEa9oGbuBEhzGoV2QjIHB90mrByxq6AicufZzLLN1iLJLgiEt3yMjHZvNt2BxSI1yjeiV2OE+XJMx1GPEE/MZKUhA9UKBZlacbcMqTX2SMe1RfH7cNy6ptWzKVwV8Tlt5nS70299mXJskGNxLwwQjbu1s68gpmQIEoqR7YKBZKNjq9n66xDDKb03GY/wANLz2REjYIzi5n86WMn6CDGcwdfiaB10FvDQawLUQsU/9lyZ089477Tmu2mosA/SDgcWNR1Q665w28xzeDt+Iem+MQqOAwpdfh0qL8ioEb5Q2EYHjDuXKi87IdMpQa4tzGRmpsfoqQrMQwZ69KJ4j8/HfqkBezdWxZ4+FRhLiMe8Kyceiuziuk6Q/TXElM39M421NqWjbcv+7c470YgQ2mY8YCOijve7OPundPCs83RgYRnN5YyVZYB5cFo4pZNc5PbVj1BUpLtc1WmKyt1CIAb7RbZZkkSYwVXvv3o9fH1XFfidKYb2jAFHB5zg2DgF1SZJUM6Tc7/QqiApOxnYMHQQjqd+7nU3Ku5g97CIBrNc557C7a8gnkvdX/yrZsASQiIPCPqK/FT4/pb2dWUohJZPJgV9xyMgrUoSfNa9oozOpnuFg7Ep2IogTnQwEYPBSEvWgbftiUnHqO9kE9miu6VvDQ7KwfcE8tbM13iGpv2bIiCKLo9QGZIIt1hmKdACOObueUKAd9xIi4wZ++/O1DMf07pf1iFAUA7CBTM/W4SeCZn8Sveb7/mrImCAZJoELq4igLDR/NBnFv8cMWhIGqpqrMv/FPaylOXu/LZe5fzYwmKKyIUzfVH19vXQKk65jD73Z2gBjqIArO19FQL4TkhdyU4N49Q9iObNQWFFhL5CoiaGMvYxDR+WtJWOdI2fhCzZIYtrnohusc8IZELjZzFTclV9YqBpArHghkc4UwjJiHdu38cepbLxcJ+Sagj7IihnpZl/FSCQxHuNsSjxRqW0Q01Kt5P8PNxDWYmZvx7HJfGpOXlxwiUPjkXbA4UCKhpe5ZWAbjgxsMCCJzDQ4sf++PyFFsNsQqVdVbA5DFM8btc7uY7z7fFDcQcFVke8YoJ/F8F/Tiy8qS73fTM+lYMmJcfugPNssnJ6kQC6bfxOd8UAx/8HpeIRHACkycIgWU7JfMsEmTSZNdBtT6yEU5K7HPmw718VUBXmyz8D8wuAA==",
        "x-amz-target": "Firehose_20150804.PutRecordBatch",
        "content-type": "application/x-amz-json-1.1",
        "host": "firehose.us-east-1.amazonaws.com",
        "connection": "Keep-Alive"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)


    url = "https://firehose.us-east-1.amazonaws.com/"

    payload = "{\"DeliveryStreamName\":\"jackalope-prod-firehose\",\"Records\":[{\"Data\":\"eyJhY2N1cmFjeSI6MC4wLCJhY3Rpdml0eUNvbmZpZGVuY2UiOjAsImFjdGl2aXR5VHlwZSI6IlVua25vd24iLCJhbHRpdHVkZSI6MC4wLCJhcHBfdmVyc2lvbiI6IjQuNTUuMSIsImJlYXJpbmciOjAuMCwiYnJhemVFdmVudCI6ZmFsc2UsImNhcnJpZXIiOiJULU1vYmlsZSIsImNvdXJpZXJJZCI6ImVmN2E5ZjdkLTg1ZjEtNGI0NS1hMjg0LTM5YmIzZjQ4YTE4MCIsImN1cnJlbnRDaGFyZ2UiOjEwMCwiZGV2aWNlTWFudWZhY3R1cmVyIjoiR29vZ2xlIiwiZGV2aWNlTW9kZWwiOiJzZGtfZ3Bob25lNjRfYXJtNjQiLCJkZXZpY2VfaWQiOiI3YjRiMTViYi02MWFlLTQ5NjAtOTJjZi0wMjNkYWY1M2E2ZDQiLCJkcml2ZXJJZCI6ImVmN2E5ZjdkLTg1ZjEtNGI0NS1hMjg0LTM5YmIzZjQ4YTE4MCIsImV2ZW50Q2F0ZWdvcnkiOiJzY2hlZHVsaW5nIiwiZXZlbnRMYWJlbCI6ImJsb2Nrc19kcm9wcGVkX3RoaXNfc2Vzc2lvbiIsImlzQ2hhcmdpbmciOmZhbHNlLCJpc0Zyb21Nb2NrTG9jYXRpb25Qcm92aWRlciI6ZmFsc2UsImlzSW5Gb3JlZ3JvdW5kIjp0cnVlLCJpc05lb24iOnRydWUsImxhdExuZyI6Ik5BIiwibGF0aXR1ZGUiOjAuMCwibG9uZ2l0dWRlIjowLjAsIm1lc3NhZ2UiOiIwIiwibm90aWZpY2F0aW9uQ2F0ZWdvcnkiOiJOL0EiLCJub3RpZmljYXRpb25JZCI6Ik5BIiwib3JkZXJJZCI6Ik5BIiwib3MiOiIyMjIiLCJwaG9uZVR5cGUiOiJBbmRyb2lkLCAzMyIsInBsYXRmb3JtIjoiQW5kcm9pZCIsInJlZ2lvbklkIjoiNDY4NmQ0MmUtYjliZC00YmMwLWE4ODctYzVlOGZiNzhlMmJlIiwicmVxdWVzdCI6Ik5BIiwic3BlZWQiOjAuMCwidGltZVNlbnQiOiJOL0EiLCJ0aW1lc3RhbXAiOiIyMDIzMDMwNlQyMzEyMDAuMTA3WiIsInRyaXBJZCI6Ik5BIiwid2F5cG9pbnRJZCI6Ik5BIn0K\"},{\"Data\":\"eyJhY2N1cmFjeSI6MC4wLCJhY3Rpdml0eUNvbmZpZGVuY2UiOjAsImFjdGl2aXR5VHlwZSI6IlVua25vd24iLCJhbHRpdHVkZSI6MC4wLCJhcHBfdmVyc2lvbiI6IjQuNTUuMSIsImJlYXJpbmciOjAuMCwiYnJhemVFdmVudCI6ZmFsc2UsImNhcnJpZXIiOiJULU1vYmlsZSIsImNvdXJpZXJJZCI6ImVmN2E5ZjdkLTg1ZjEtNGI0NS1hMjg0LTM5YmIzZjQ4YTE4MCIsImN1cnJlbnRDaGFyZ2UiOjEwMCwiZGV2aWNlTWFudWZhY3R1cmVyIjoiR29vZ2xlIiwiZGV2aWNlTW9kZWwiOiJzZGtfZ3Bob25lNjRfYXJtNjQiLCJkZXZpY2VfaWQiOiI3YjRiMTViYi02MWFlLTQ5NjAtOTJjZi0wMjNkYWY1M2E2ZDQiLCJkcml2ZXJJZCI6ImVmN2E5ZjdkLTg1ZjEtNGI0NS1hMjg0LTM5YmIzZjQ4YTE4MCIsImV2ZW50Q2F0ZWdvcnkiOiJzY2hlZHVsaW5nIiwiZXZlbnRMYWJlbCI6ImJsb2Nrc19hZGRlZF90aGlzX3Nlc3Npb24iLCJpc0NoYXJnaW5nIjpmYWxzZSwiaXNGcm9tTW9ja0xvY2F0aW9uUHJvdmlkZXIiOmZhbHNlLCJpc0luRm9yZWdyb3VuZCI6dHJ1ZSwiaXNOZW9uIjp0cnVlLCJsYXRMbmciOiJOQSIsImxhdGl0dWRlIjowLjAsImxvbmdpdHVkZSI6MC4wLCJtZXNzYWdlIjoiMSIsIm5vdGlmaWNhdGlvbkNhdGVnb3J5IjoiTi9BIiwibm90aWZpY2F0aW9uSWQiOiJOQSIsIm9yZGVySWQiOiJOQSIsIm9zIjoiMjIyIiwicGhvbmVUeXBlIjoiQW5kcm9pZCwgMzMiLCJwbGF0Zm9ybSI6IkFuZHJvaWQiLCJyZWdpb25JZCI6IjQ2ODZkNDJlLWI5YmQtNGJjMC1hODg3LWM1ZThmYjc4ZTJiZSIsInJlcXVlc3QiOiJOQSIsInNwZWVkIjowLjAsInRpbWVTZW50IjoiTi9BIiwidGltZXN0YW1wIjoiMjAyMzAzMDZUMjMxMjAwLjEwNloiLCJ0cmlwSWQiOiJOQSIsIndheXBvaW50SWQiOiJOQSJ9Cg==\"},{\"Data\":\"eyJhY2N1cmFjeSI6MC4wLCJhY3Rpdml0eUNvbmZpZGVuY2UiOjAsImFjdGl2aXR5VHlwZSI6IlVua25vd24iLCJhbHRpdHVkZSI6MC4wLCJhcHBfdmVyc2lvbiI6IjQuNTUuMSIsImJlYXJpbmciOjAuMCwiYnJhemVFdmVudCI6dHJ1ZSwiY2FycmllciI6IlQtTW9iaWxlIiwiY291cmllcklkIjoiZWY3YTlmN2QtODVmMS00YjQ1LWEyODQtMzliYjNmNDhhMTgwIiwiY3VycmVudENoYXJnZSI6MTAwLCJkZXZpY2VNYW51ZmFjdHVyZXIiOiJHb29nbGUiLCJkZXZpY2VNb2RlbCI6InNka19ncGhvbmU2NF9hcm02NCIsImRldmljZV9pZCI6IjdiNGIxNWJiLTYxYWUtNDk2MC05MmNmLTAyM2RhZjUzYTZkNCIsImRyaXZlcklkIjoiZWY3YTlmN2QtODVmMS00YjQ1LWEyODQtMzliYjNmNDhhMTgwIiwiZXZlbnRDYXRlZ29yeSI6InNjaGVkdWxpbmciLCJldmVudExhYmVsIjoiZG9uZV91cGRhdGluZ19zY2hlZHVsZSIsImlzQ2hhcmdpbmciOmZhbHNlLCJpc0Zyb21Nb2NrTG9jYXRpb25Qcm92aWRlciI6ZmFsc2UsImlzSW5Gb3JlZ3JvdW5kIjp0cnVlLCJpc05lb24iOnRydWUsImxhdExuZyI6Ik5BIiwibGF0aXR1ZGUiOjAuMCwibG9uZ2l0dWRlIjowLjAsIm1lc3NhZ2UiOiIzMiIsIm5vdGlmaWNhdGlvbkNhdGVnb3J5IjoiTi9BIiwibm90aWZpY2F0aW9uSWQiOiJOQSIsIm9yZGVySWQiOiJOQSIsIm9zIjoiMjIyIiwicGhvbmVUeXBlIjoiQW5kcm9pZCwgMzMiLCJwbGF0Zm9ybSI6IkFuZHJvaWQiLCJyZWdpb25JZCI6IjQ2ODZkNDJlLWI5YmQtNGJjMC1hODg3LWM1ZThmYjc4ZTJiZSIsInJlcXVlc3QiOiJOQSIsInNwZWVkIjowLjAsInRpbWVTZW50IjoiTi9BIiwidGltZXN0YW1wIjoiMjAyMzAzMDZUMjMxMjAwLjEwNloiLCJ0cmlwSWQiOiJOQSIsIndheXBvaW50SWQiOiJOQSJ9Cg==\"}]}"
    headers = {
        "x-newrelic-id": "VQQDVlBVGwEFUVZRBAMBVQ==",
        "authorization": "AWS4-HMAC-SHA256 Credential=ASIAVEHGYS4FH5U3NA45/20230307/us-east-1/firehose/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token;x-amz-target, Signature=2d6acb3a51a50e893c5bd4026cfed8abb3db76eb416f96628ceb8c9a607a1a3d",
        "x-amz-date": "20230307T171529Z",
        "aws-sdk-invocation-id": "280f16de-451b-4b2b-96f9-e72a3704590f",
        "content-encoding": "gzip",
        "user-agent": "aws-sdk-android/2.16.8 Linux/5.15.41-android13-8-00205-gf1bf82c3dacd-ab8747247 Dalvik/2.1.0/0 en_US com.amazonaws.mobileconnectors.kinesis.kinesisrecorder.KinesisFirehoseRecorder/2.16.8",
        "aws-sdk-retry": "0/0",
        "accept-encoding": "identity",
        "x-amz-security-token": "IQoJb3JpZ2luX2VjEHoaCXVzLWVhc3QtMSJGMEQCIGjx+BlZrGnY0m1QTpzxQTA7YjEat7+qu5oq8FDxyB8mAiBHzm1PjsD0EShQb9OsmPyDrJ8oNxpSgxnkaimqDDDkgyqSBggyEAYaDDM1MjY3MTI3NDc2MiIM2okl0AGZvuQDSWfRKu8F8teE7HG8b7fxyhM5I7n3mwHMHl1FGuxAfBK8KrG5zp1DW9TfmWfFmeiHPcQa+MmymLxYDuc/Aig/A637hwMj4Iay/Wm8hi/+HEu2C9Sx9O8B5TDnQ82c542B5zD3avaMiAzB3BLT+Gcjt5TnYQRMvzA/Jv0dB/YklSkU9RiHhPzJSJEa9oGbuBEhzGoV2QjIHB90mrByxq6AicufZzLLN1iLJLgiEt3yMjHZvNt2BxSI1yjeiV2OE+XJMx1GPEE/MZKUhA9UKBZlacbcMqTX2SMe1RfH7cNy6ptWzKVwV8Tlt5nS70299mXJskGNxLwwQjbu1s68gpmQIEoqR7YKBZKNjq9n66xDDKb03GY/wANLz2REjYIzi5n86WMn6CDGcwdfiaB10FvDQawLUQsU/9lyZ089477Tmu2mosA/SDgcWNR1Q665w28xzeDt+Iem+MQqOAwpdfh0qL8ioEb5Q2EYHjDuXKi87IdMpQa4tzGRmpsfoqQrMQwZ69KJ4j8/HfqkBezdWxZ4+FRhLiMe8Kyceiuziuk6Q/TXElM39M421NqWjbcv+7c470YgQ2mY8YCOijve7OPundPCs83RgYRnN5YyVZYB5cFo4pZNc5PbVj1BUpLtc1WmKyt1CIAb7RbZZkkSYwVXvv3o9fH1XFfidKYb2jAFHB5zg2DgF1SZJUM6Tc7/QqiApOxnYMHQQjqd+7nU3Ku5g97CIBrNc557C7a8gnkvdX/yrZsASQiIPCPqK/FT4/pb2dWUohJZPJgV9xyMgrUoSfNa9oozOpnuFg7Ep2IogTnQwEYPBSEvWgbftiUnHqO9kE9miu6VvDQ7KwfcE8tbM13iGpv2bIiCKLo9QGZIIt1hmKdACOObueUKAd9xIi4wZ++/O1DMf07pf1iFAUA7CBTM/W4SeCZn8Sveb7/mrImCAZJoELq4igLDR/NBnFv8cMWhIGqpqrMv/FPaylOXu/LZe5fzYwmKKyIUzfVH19vXQKk65jD73Z2gBjqIArO19FQL4TkhdyU4N49Q9iObNQWFFhL5CoiaGMvYxDR+WtJWOdI2fhCzZIYtrnohusc8IZELjZzFTclV9YqBpArHghkc4UwjJiHdu38cepbLxcJ+Sagj7IihnpZl/FSCQxHuNsSjxRqW0Q01Kt5P8PNxDWYmZvx7HJfGpOXlxwiUPjkXbA4UCKhpe5ZWAbjgxsMCCJzDQ4sf++PyFFsNsQqVdVbA5DFM8btc7uY7z7fFDcQcFVke8YoJ/F8F/Tiy8qS73fTM+lYMmJcfugPNssnJ6kQC6bfxOd8UAx/8HpeIRHACkycIgWU7JfMsEmTSZNdBtT6yEU5K7HPmw718VUBXmyz8D8wuAA==",
        "x-amz-target": "Firehose_20150804.PutRecordBatch",
        "content-type": "application/x-amz-json-1.1",
        "host": "firehose.us-east-1.amazonaws.com",
        "connection": "Keep-Alive"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)