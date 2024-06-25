import streamlit as st
import numpy as np

def calculate_pressure(diameter_inches, length, max_altitude, profile):
    """
    Calculates the pressure at the lowest point of a flexible pipe.

    Args:
        diameter_inches (float): Diameter of the pipe in inches.
        length (float): Length of the pipe in meters.
        max_altitude (float): Maximum altitude of the pipe in meters.
        profile (list[float]): List of altitude values along the pipe profile in meters.

    Returns:
        float: Pressure at the lowest point in kilopascals (kPa).
    """

    # Convert diameter from inches to meters
    diameter_meters = diameter_inches * 0.0254

    # Calculate the cross-sectional area of the pipe
    area = np.pi * (diameter_meters / 2) ** 2

    # Calculate the density of water
    water_density = 1000  # kg/m^3

    # Calculate the acceleration due to gravity
    gravity = 9.81  # m/s^2

    # Calculate the minimum altitude
    min_altitude = max_altitude - min(profile)

    # Calculate the pressure difference
    pressure_difference = water_density * gravity * (max_altitude - min_altitude)

    # Calculate the pressure at the lowest point
    pressure = pressure_difference / area

    return pressure * 1000  # Convert from Pa to kPa

def main():
    st.title("Calculadora de presión en tuberías flexibles")

    # Select pipe diameter
    diameter_option = st.selectbox("Diámetro de la tubería:", ["10 pulgadas", "12 pulgadas"])
    if diameter_option == "10 pulgadas":
        diameter_inches = 10
    else:
        diameter_inches = 12

    # Input length and maximum altitude
    length = st.number_input("Longitud de la tubería (en metros):")
    max_altitude = st
