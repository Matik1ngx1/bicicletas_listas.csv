import os 
import streamlit as st
import pandas as pd


df = pd.read_csv("bicicletas_listas.csv", sep=";", encoding="utf-8-sig")
