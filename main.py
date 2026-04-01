import json, unittest, datetime

with open("./data-1.json","r", encoding="utf-8") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r", encoding="utf-8") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r", encoding="utf-8") as f:
    jsonExpectedResult = json.load(f)

def convertFromFormat1(jsonObject):
    locationParts = jsonObject["location"].split("/")
    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": locationParts[0],
            "city": locationParts[1],
            "area": locationParts[2],
            "factory": locationParts[3],
            "section": locationParts[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }

def convertFromFormat2(jsonObject):
    dt = datetime.datetime.strptime(
        jsonObject["timestamp"],
        "%Y-%m-%dT%H:%M:%S.%fZ"
    ).replace(tzinfo=datetime.timezone.utc)

    timestamp = int(dt.timestamp() * 1000)

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": timestamp,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },
        "data": {
            "status": jsonObject["data"]["status"],
            "temperature": jsonObject["data"]["temperature"]
        }
    }

def main(jsonObject):
    if jsonObject.get("device") is None:
        return convertFromFormat1(jsonObject)
    return convertFromFormat2(jsonObject)

class TestSolution(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(jsonExpectedResult, json.loads(json.dumps(jsonExpectedResult)))

    def test_dataType1(self):
        self.assertEqual(main(jsonData1), jsonExpectedResult)

    def test_dataType2(self):
        self.assertEqual(main(jsonData2), jsonExpectedResult)

if __name__ == "__main__":
    unittest.main()
