"""
Get your latest readings from the Abbot servers.
"""


import logging
import mcp
from mcp.server import FastMCP
from pylibrelinkup import PyLibreLinkUp
import os


mcp = FastMCP("GCM")

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


@mcp.tool()
async def get_blood_sugar():
    username = os.getenv("API_USERNAME")
    password = os.getenv("API_PASSWORD")
    libre_client = PyLibreLinkUp(email=username, password=password)
    libre_client.authenticate()
    patient_list = libre_client.get_patients()
    sensor_reading = libre_client.latest(patient_identifier=patient_list[0])
    return f"""
        Current Reading: {sensor_reading.value}
        Is High: {sensor_reading.is_high},
        Is Low: {sensor_reading.is_low},
        Trend: {sensor_reading.trend.value},
    """


@mcp.tool()
async def get_blood_sugar_history():
    username = os.getenv("API_USERNAME")
    password = os.getenv("API_PASSWORD")
    libre_client = PyLibreLinkUp(email=username, password=password)
    libre_client.authenticate()
    patient_list = libre_client.get_patients()
    measurements = libre_client.graph(patient_identifier=patient_list[0])
    readings = [
        {"timestamp": str(m.timestamp), "value": m.value, "measurement_color": m.measurement_color}
        for m in measurements
    ]
    return "\n".join(f"{r['timestamp']}  {r['value']:5.1f}  {r['measurement_color']}" for r in readings)


def main():
    # Initialize and run the server
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
