from main import get_weather

def test_get_weather_warm():
    assert get_weather(25) == "It's warm outside!"
     