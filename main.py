import openai
import streamlit as st
import textwrap
with open('style.css') as f:
   st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
   
st.title("Mental Health Chatbot")

bg = '''
.magicpattern { 
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
  background-repeat: repeat;
  background-image: url("data:image/svg+xml;utf8,%3Csvg viewBox=%220 0 2000 3000%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cmask id=%22b%22 x=%220%22 y=%220%22 width=%222000%22 height=%223000%22%3E%3Cpath fill=%22url(%23a)%22 d=%22M0 0h2000v3000H0z%22%2F%3E%3C%2Fmask%3E%3Cpath fill=%22%231b0036%22 d=%22M0 0h2000v3000H0z%22%2F%3E%3Cg style=%22transform-origin:center center%22 stroke=%22%234c6e47%22 stroke-width=%223%22 mask=%22url(%23b)%22%3E%3Cpath fill=%22none%22 d=%22M0 0h100v100H0zM100 0h100v100H100zM200 0h100v100H200zM300 0h100v100H300zM400 0h100v100H400z%22%2F%3E%3Cpath fill=%22%234c6e4770%22 d=%22M500 0h100v100H500z%22%2F%3E%3Cpath fill=%22none%22 d=%22M600 0h100v100H600zM700 0h100v100H700zM800 0h100v100H800zM900 0h100v100H900zM1000 0h100v100h-100zM1100 0h100v100h-100zM1200 0h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4781%22 d=%22M1300 0h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1400 0h100v100h-100zM1500 0h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e474a%22 d=%22M1600 0h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1700 0h100v100h-100zM1800 0h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47b6%22 d=%22M1900 0h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M0 100h100v100H0zM100 100h100v100H100z%22%2F%3E%3Cpath fill=%22%234c6e47dd%22 d=%22M200 100h100v100H200z%22%2F%3E%3Cpath fill=%22%234c6e4703%22 d=%22M300 100h100v100H300z%22%2F%3E%3Cpath fill=%22none%22 d=%22M400 100h100v100H400zM500 100h100v100H500z%22%2F%3E%3Cpath fill=%22%234c6e4712%22 d=%22M600 100h100v100H600z%22%2F%3E%3Cpath fill=%22%234c6e4799%22 d=%22M700 100h100v100H700z%22%2F%3E%3Cpath fill=%22none%22 d=%22M800 100h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e4772%22 d=%22M900 100h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e47d9%22 d=%22M1000 100h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1100 100h100v100h-100zM1200 100h100v100h-100zM1300 100h100v100h-100zM1400 100h100v100h-100zM1500 100h100v100h-100zM1600 100h100v100h-100zM1700 100h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47e8%22 d=%22M1800 100h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1900 100h100v100h-100zM0 200h100v100H0zM100 200h100v100H100zM200 200h100v100H200zM300 200h100v100H300zM400 200h100v100H400zM500 200h100v100H500zM600 200h100v100H600zM700 200h100v100H700z%22%2F%3E%3Cpath fill=%22%234c6e47a1%22 d=%22M800 200h100v100H800z%22%2F%3E%3Cpath fill=%22none%22 d=%22M900 200h100v100H900zM1000 200h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47dc%22 d=%22M1100 200h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1200 200h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47ab%22 d=%22M1300 200h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1400 200h100v100h-100zM1500 200h100v100h-100zM1600 200h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e475e%22 d=%22M1700 200h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47ad%22 d=%22M1800 200h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4795%22 d=%22M1900 200h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M0 300h100v100H0zM100 300h100v100H100zM200 300h100v100H200zM300 300h100v100H300zM400 300h100v100H400zM500 300h100v100H500zM600 300h100v100H600zM700 300h100v100H700zM800 300h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e4753%22 d=%22M900 300h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e47a0%22 d=%22M1000 300h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4717%22 d=%22M1100 300h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1200 300h100v100h-100zM1300 300h100v100h-100zM1400 300h100v100h-100zM1500 300h100v100h-100zM1600 300h100v100h-100zM1700 300h100v100h-100zM1800 300h100v100h-100zM1900 300h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e475c%22 d=%22M0 400h100v100H0z%22%2F%3E%3Cpath fill=%22none%22 d=%22M100 400h100v100H100zM200 400h100v100H200z%22%2F%3E%3Cpath fill=%22%234c6e479d%22 d=%22M300 400h100v100H300z%22%2F%3E%3Cpath fill=%22none%22 d=%22M400 400h100v100H400z%22%2F%3E%3Cpath fill=%22%234c6e47fa%22 d=%22M500 400h100v100H500z%22%2F%3E%3Cpath fill=%22none%22 d=%22M600 400h100v100H600zM700 400h100v100H700zM800 400h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e4779%22 d=%22M900 400h100v100H900z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1000 400h100v100h-100zM1100 400h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47b5%22 d=%22M1200 400h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1300 400h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4771%22 d=%22M1400 400h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47b2%22 d=%22M1500 400h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1600 400h100v100h-100zM1700 400h100v100h-100zM1800 400h100v100h-100zM1900 400h100v100h-100zM0 500h100v100H0zM100 500h100v100H100zM200 500h100v100H200zM300 500h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e4728%22 d=%22M400 500h100v100H400z%22%2F%3E%3Cpath fill=%22%234c6e4719%22 d=%22M500 500h100v100H500z%22%2F%3E%3Cpath fill=%22none%22 d=%22M600 500h100v100H600zM700 500h100v100H700z%22%2F%3E%3Cpath fill=%22%234c6e47f8%22 d=%22M800 500h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e47e7%22 d=%22M900 500h100v100H900z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1000 500h100v100h-100zM1100 500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e475f%22 d=%22M1200 500h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1300 500h100v100h-100zM1400 500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47f7%22 d=%22M1500 500h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1600 500h100v100h-100zM1700 500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4703%22 d=%22M1800 500h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1900 500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4736%22 d=%22M0 600h100v100H0z%22%2F%3E%3Cpath fill=%22none%22 d=%22M100 600h100v100H100zM200 600h100v100H200zM300 600h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e4717%22 d=%22M400 600h100v100H400z%22%2F%3E%3Cpath fill=%22%234c6e477b%22 d=%22M500 600h100v100H500z%22%2F%3E%3Cpath fill=%22%234c6e4777%22 d=%22M600 600h100v100H600z%22%2F%3E%3Cpath fill=%22none%22 d=%22M700 600h100v100H700zM800 600h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e47a4%22 d=%22M900 600h100v100H900z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1000 600h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47f0%22 d=%22M1100 600h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1200 600h100v100h-100zM1300 600h100v100h-100zM1400 600h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47b4%22 d=%22M1500 600h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1600 600h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4786%22 d=%22M1700 600h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1800 600h100v100h-100zM1900 600h100v100h-100zM0 700h100v100H0zM100 700h100v100H100zM200 700h100v100H200zM300 700h100v100H300zM400 700h100v100H400zM500 700h100v100H500zM600 700h100v100H600zM700 700h100v100H700z%22%2F%3E%3Cpath fill=%22%234c6e4779%22 d=%22M800 700h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e4733%22 d=%22M900 700h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e4711%22 d=%22M1000 700h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1100 700h100v100h-100zM1200 700h100v100h-100zM1300 700h100v100h-100zM1400 700h100v100h-100zM1500 700h100v100h-100zM1600 700h100v100h-100zM1700 700h100v100h-100zM1800 700h100v100h-100zM1900 700h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e474c%22 d=%22M0 800h100v100H0z%22%2F%3E%3Cpath fill=%22none%22 d=%22M100 800h100v100H100zM200 800h100v100H200zM300 800h100v100H300zM400 800h100v100H400z%22%2F%3E%3Cpath fill=%22%234c6e47e8%22 d=%22M500 800h100v100H500z%22%2F%3E%3Cpath fill=%22none%22 d=%22M600 800h100v100H600zM700 800h100v100H700zM800 800h100v100H800zM900 800h100v100H900zM1000 800h100v100h-100zM1100 800h100v100h-100zM1200 800h100v100h-100zM1300 800h100v100h-100zM1400 800h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4772%22 d=%22M1500 800h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1600 800h100v100h-100zM1700 800h100v100h-100zM1800 800h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e476f%22 d=%22M1900 800h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M0 900h100v100H0zM100 900h100v100H100zM200 900h100v100H200z%22%2F%3E%3Cpath fill=%22%234c6e4769%22 d=%22M300 900h100v100H300z%22%2F%3E%3Cpath fill=%22none%22 d=%22M400 900h100v100H400zM500 900h100v100H500zM600 900h100v100H600zM700 900h100v100H700zM800 900h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e475f%22 d=%22M900 900h100v100H900z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1000 900h100v100h-100zM1100 900h100v100h-100zM1200 900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4769%22 d=%22M1300 900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4722%22 d=%22M1400 900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47ec%22 d=%22M1500 900h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1600 900h100v100h-100zM1700 900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4783%22 d=%22M1800 900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47a0%22 d=%22M1900 900h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M0 1000h100v100H0zM100 1000h100v100H100zM200 1000h100v100H200zM300 1000h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e47ca%22 d=%22M400 1000h100v100H400z%22%2F%3E%3Cpath fill=%22none%22 d=%22M500 1000h100v100H500z%22%2F%3E%3Cpath fill=%22%234c6e479f%22 d=%22M600 1000h100v100H600z%22%2F%3E%3Cpath fill=%22none%22 d=%22M700 1000h100v100H700z%22%2F%3E%3Cpath fill=%22%234c6e471c%22 d=%22M800 1000h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e4764%22 d=%22M900 1000h100v100H900z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1000 1000h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4731%22 d=%22M1100 1000h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47a0%22 d=%22M1200 1000h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1300 1000h100v100h-100zM1400 1000h100v100h-100zM1500 1000h100v100h-100zM1600 1000h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e475b%22 d=%22M1700 1000h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4794%22 d=%22M1800 1000h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4702%22 d=%22M1900 1000h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M0 1100h100v100H0zM100 1100h100v100H100zM200 1100h100v100H200z%22%2F%3E%3Cpath fill=%22%234c6e4759%22 d=%22M300 1100h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e4799%22 d=%22M400 1100h100v100H400z%22%2F%3E%3Cpath fill=%22%234c6e47f4%22 d=%22M500 1100h100v100H500z%22%2F%3E%3Cpath fill=%22none%22 d=%22M600 1100h100v100H600zM700 1100h100v100H700zM800 1100h100v100H800zM900 1100h100v100H900zM1000 1100h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e473d%22 d=%22M1100 1100h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47c5%22 d=%22M1200 1100h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1300 1100h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47bb%22 d=%22M1400 1100h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1500 1100h100v100h-100zM1600 1100h100v100h-100zM1700 1100h100v100h-100zM1800 1100h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47d2%22 d=%22M1900 1100h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M0 1200h100v100H0zM100 1200h100v100H100zM200 1200h100v100H200zM300 1200h100v100H300zM400 1200h100v100H400zM500 1200h100v100H500zM600 1200h100v100H600zM700 1200h100v100H700z%22%2F%3E%3Cpath fill=%22%234c6e475f%22 d=%22M800 1200h100v100H800z%22%2F%3E%3Cpath fill=%22none%22 d=%22M900 1200h100v100H900zM1000 1200h100v100h-100zM1100 1200h100v100h-100zM1200 1200h100v100h-100zM1300 1200h100v100h-100zM1400 1200h100v100h-100zM1500 1200h100v100h-100zM1600 1200h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4758%22 d=%22M1700 1200h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1800 1200h100v100h-100zM1900 1200h100v100h-100zM0 1300h100v100H0z%22%2F%3E%3Cpath fill=%22%234c6e47a8%22 d=%22M100 1300h100v100H100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M200 1300h100v100H200zM300 1300h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e4732%22 d=%22M400 1300h100v100H400z%22%2F%3E%3Cpath fill=%22none%22 d=%22M500 1300h100v100H500z%22%2F%3E%3Cpath fill=%22%234c6e47cc%22 d=%22M600 1300h100v100H600z%22%2F%3E%3Cpath fill=%22none%22 d=%22M700 1300h100v100H700zM800 1300h100v100H800zM900 1300h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e475d%22 d=%22M1000 1300h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1100 1300h100v100h-100zM1200 1300h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47dc%22 d=%22M1300 1300h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4711%22 d=%22M1400 1300h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47d3%22 d=%22M1500 1300h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1600 1300h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e477e%22 d=%22M1700 1300h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1800 1300h100v100h-100zM1900 1300h100v100h-100zM0 1400h100v100H0zM100 1400h100v100H100z%22%2F%3E%3Cpath fill=%22%234c6e478c%22 d=%22M200 1400h100v100H200z%22%2F%3E%3Cpath fill=%22%234c6e47ea%22 d=%22M300 1400h100v100H300z%22%2F%3E%3Cpath fill=%22none%22 d=%22M400 1400h100v100H400zM500 1400h100v100H500zM600 1400h100v100H600zM700 1400h100v100H700zM800 1400h100v100H800zM900 1400h100v100H900zM1000 1400h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4764%22 d=%22M1100 1400h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1200 1400h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47a5%22 d=%22M1300 1400h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47b5%22 d=%22M1400 1400h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4796%22 d=%22M1500 1400h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4781%22 d=%22M1600 1400h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1700 1400h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4757%22 d=%22M1800 1400h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1900 1400h100v100h-100zM0 1500h100v100H0zM100 1500h100v100H100zM200 1500h100v100H200zM300 1500h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e476d%22 d=%22M400 1500h100v100H400z%22%2F%3E%3Cpath fill=%22%234c6e47ef%22 d=%22M500 1500h100v100H500z%22%2F%3E%3Cpath fill=%22%234c6e4715%22 d=%22M600 1500h100v100H600z%22%2F%3E%3Cpath fill=%22none%22 d=%22M700 1500h100v100H700zM800 1500h100v100H800zM900 1500h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e4756%22 d=%22M1000 1500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4743%22 d=%22M1100 1500h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1200 1500h100v100h-100zM1300 1500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4710%22 d=%22M1400 1500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47da%22 d=%22M1500 1500h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1600 1500h100v100h-100zM1700 1500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4792%22 d=%22M1800 1500h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1900 1500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4717%22 d=%22M0 1600h100v100H0z%22%2F%3E%3Cpath fill=%22%234c6e47c4%22 d=%22M100 1600h100v100H100z%22%2F%3E%3Cpath fill=%22%234c6e4708%22 d=%22M200 1600h100v100H200z%22%2F%3E%3Cpath fill=%22none%22 d=%22M300 1600h100v100H300zM400 1600h100v100H400zM500 1600h100v100H500zM600 1600h100v100H600zM700 1600h100v100H700z%22%2F%3E%3Cpath fill=%22%234c6e472f%22 d=%22M800 1600h100v100H800z%22%2F%3E%3Cpath fill=%22none%22 d=%22M900 1600h100v100H900zM1000 1600h100v100h-100zM1100 1600h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47d6%22 d=%22M1200 1600h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1300 1600h100v100h-100zM1400 1600h100v100h-100zM1500 1600h100v100h-100zM1600 1600h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47a0%22 d=%22M1700 1600h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1800 1600h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47ba%22 d=%22M1900 1600h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M0 1700h100v100H0zM100 1700h100v100H100zM200 1700h100v100H200zM300 1700h100v100H300zM400 1700h100v100H400zM500 1700h100v100H500z%22%2F%3E%3Cpath fill=%22%234c6e4749%22 d=%22M600 1700h100v100H600z%22%2F%3E%3Cpath fill=%22none%22 d=%22M700 1700h100v100H700zM800 1700h100v100H800zM900 1700h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e4726%22 d=%22M1000 1700h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1100 1700h100v100h-100zM1200 1700h100v100h-100zM1300 1700h100v100h-100zM1400 1700h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e472c%22 d=%22M1500 1700h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47af%22 d=%22M1600 1700h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1700 1700h100v100h-100zM1800 1700h100v100h-100zM1900 1700h100v100h-100zM0 1800h100v100H0zM100 1800h100v100H100zM200 1800h100v100H200zM300 1800h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e47af%22 d=%22M400 1800h100v100H400z%22%2F%3E%3Cpath fill=%22%234c6e4798%22 d=%22M500 1800h100v100H500z%22%2F%3E%3Cpath fill=%22none%22 d=%22M600 1800h100v100H600z%22%2F%3E%3Cpath fill=%22%234c6e478a%22 d=%22M700 1800h100v100H700z%22%2F%3E%3Cpath fill=%22none%22 d=%22M800 1800h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e4758%22 d=%22M900 1800h100v100H900z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1000 1800h100v100h-100zM1100 1800h100v100h-100zM1200 1800h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47b7%22 d=%22M1300 1800h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1400 1800h100v100h-100zM1500 1800h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4737%22 d=%22M1600 1800h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4750%22 d=%22M1700 1800h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4710%22 d=%22M1800 1800h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e471c%22 d=%22M1900 1800h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e476b%22 d=%22M0 1900h100v100H0z%22%2F%3E%3Cpath fill=%22%234c6e47ab%22 d=%22M100 1900h100v100H100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M200 1900h100v100H200zM300 1900h100v100H300zM400 1900h100v100H400zM500 1900h100v100H500z%22%2F%3E%3Cpath fill=%22%234c6e47b3%22 d=%22M600 1900h100v100H600z%22%2F%3E%3Cpath fill=%22%234c6e4791%22 d=%22M700 1900h100v100H700z%22%2F%3E%3Cpath fill=%22none%22 d=%22M800 1900h100v100H800zM900 1900h100v100H900zM1000 1900h100v100h-100zM1100 1900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e478d%22 d=%22M1200 1900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e471a%22 d=%22M1300 1900h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1400 1900h100v100h-100zM1500 1900h100v100h-100zM1600 1900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47c5%22 d=%22M1700 1900h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1800 1900h100v100h-100zM1900 1900h100v100h-100zM0 2000h100v100H0z%22%2F%3E%3Cpath fill=%22%234c6e47be%22 d=%22M100 2000h100v100H100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M200 2000h100v100H200z%22%2F%3E%3Cpath fill=%22%234c6e479f%22 d=%22M300 2000h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e470c%22 d=%22M400 2000h100v100H400z%22%2F%3E%3Cpath fill=%22%234c6e471b%22 d=%22M500 2000h100v100H500z%22%2F%3E%3Cpath fill=%22none%22 d=%22M600 2000h100v100H600z%22%2F%3E%3Cpath fill=%22%234c6e4711%22 d=%22M700 2000h100v100H700z%22%2F%3E%3Cpath fill=%22%234c6e4713%22 d=%22M800 2000h100v100H800z%22%2F%3E%3Cpath fill=%22none%22 d=%22M900 2000h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e47eb%22 d=%22M1000 2000h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1100 2000h100v100h-100zM1200 2000h100v100h-100zM1300 2000h100v100h-100zM1400 2000h100v100h-100zM1500 2000h100v100h-100zM1600 2000h100v100h-100zM1700 2000h100v100h-100zM1800 2000h100v100h-100zM1900 2000h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e476b%22 d=%22M0 2100h100v100H0z%22%2F%3E%3Cpath fill=%22none%22 d=%22M100 2100h100v100H100zM200 2100h100v100H200z%22%2F%3E%3Cpath fill=%22%234c6e47b9%22 d=%22M300 2100h100v100H300z%22%2F%3E%3Cpath fill=%22none%22 d=%22M400 2100h100v100H400zM500 2100h100v100H500z%22%2F%3E%3Cpath fill=%22%234c6e4748%22 d=%22M600 2100h100v100H600z%22%2F%3E%3Cpath fill=%22none%22 d=%22M700 2100h100v100H700zM800 2100h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e4733%22 d=%22M900 2100h100v100H900z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1000 2100h100v100h-100zM1100 2100h100v100h-100zM1200 2100h100v100h-100zM1300 2100h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47f7%22 d=%22M1400 2100h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1500 2100h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4780%22 d=%22M1600 2100h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1700 2100h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4776%22 d=%22M1800 2100h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1900 2100h100v100h-100zM0 2200h100v100H0zM100 2200h100v100H100zM200 2200h100v100H200z%22%2F%3E%3Cpath fill=%22%234c6e47a5%22 d=%22M300 2200h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e47ff%22 d=%22M400 2200h100v100H400z%22%2F%3E%3Cpath fill=%22none%22 d=%22M500 2200h100v100H500zM600 2200h100v100H600zM700 2200h100v100H700zM800 2200h100v100H800zM900 2200h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e47cd%22 d=%22M1000 2200h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1100 2200h100v100h-100zM1200 2200h100v100h-100zM1300 2200h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4747%22 d=%22M1400 2200h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4755%22 d=%22M1500 2200h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1600 2200h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4710%22 d=%22M1700 2200h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1800 2200h100v100h-100zM1900 2200h100v100h-100zM0 2300h100v100H0zM100 2300h100v100H100zM200 2300h100v100H200zM300 2300h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e479d%22 d=%22M400 2300h100v100H400z%22%2F%3E%3Cpath fill=%22none%22 d=%22M500 2300h100v100H500z%22%2F%3E%3Cpath fill=%22%234c6e4793%22 d=%22M600 2300h100v100H600z%22%2F%3E%3Cpath fill=%22%234c6e47dc%22 d=%22M700 2300h100v100H700z%22%2F%3E%3Cpath fill=%22%234c6e472e%22 d=%22M800 2300h100v100H800z%22%2F%3E%3Cpath fill=%22none%22 d=%22M900 2300h100v100H900zM1000 2300h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4762%22 d=%22M1100 2300h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1200 2300h100v100h-100zM1300 2300h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47e0%22 d=%22M1400 2300h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1500 2300h100v100h-100zM1600 2300h100v100h-100zM1700 2300h100v100h-100zM1800 2300h100v100h-100zM1900 2300h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4710%22 d=%22M0 2400h100v100H0z%22%2F%3E%3Cpath fill=%22%234c6e47b9%22 d=%22M100 2400h100v100H100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M200 2400h100v100H200z%22%2F%3E%3Cpath fill=%22%234c6e4737%22 d=%22M300 2400h100v100H300z%22%2F%3E%3Cpath fill=%22none%22 d=%22M400 2400h100v100H400zM500 2400h100v100H500zM600 2400h100v100H600zM700 2400h100v100H700z%22%2F%3E%3Cpath fill=%22%234c6e4717%22 d=%22M800 2400h100v100H800z%22%2F%3E%3Cpath fill=%22none%22 d=%22M900 2400h100v100H900zM1000 2400h100v100h-100zM1100 2400h100v100h-100zM1200 2400h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4757%22 d=%22M1300 2400h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1400 2400h100v100h-100zM1500 2400h100v100h-100zM1600 2400h100v100h-100zM1700 2400h100v100h-100zM1800 2400h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47c9%22 d=%22M1900 2400h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M0 2500h100v100H0z%22%2F%3E%3Cpath fill=%22%234c6e4729%22 d=%22M100 2500h100v100H100z%22%2F%3E%3Cpath fill=%22%234c6e4707%22 d=%22M200 2500h100v100H200z%22%2F%3E%3Cpath fill=%22none%22 d=%22M300 2500h100v100H300zM400 2500h100v100H400zM500 2500h100v100H500zM600 2500h100v100H600zM700 2500h100v100H700z%22%2F%3E%3Cpath fill=%22%234c6e4726%22 d=%22M800 2500h100v100H800z%22%2F%3E%3Cpath fill=%22none%22 d=%22M900 2500h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e47b8%22 d=%22M1000 2500h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1100 2500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4789%22 d=%22M1200 2500h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1300 2500h100v100h-100zM1400 2500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e471b%22 d=%22M1500 2500h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1600 2500h100v100h-100zM1700 2500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47f0%22 d=%22M1800 2500h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4785%22 d=%22M1900 2500h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M0 2600h100v100H0zM100 2600h100v100H100zM200 2600h100v100H200zM300 2600h100v100H300zM400 2600h100v100H400zM500 2600h100v100H500zM600 2600h100v100H600z%22%2F%3E%3Cpath fill=%22%234c6e47d5%22 d=%22M700 2600h100v100H700z%22%2F%3E%3Cpath fill=%22none%22 d=%22M800 2600h100v100H800zM900 2600h100v100H900zM1000 2600h100v100h-100zM1100 2600h100v100h-100zM1200 2600h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47d1%22 d=%22M1300 2600h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1400 2600h100v100h-100zM1500 2600h100v100h-100zM1600 2600h100v100h-100zM1700 2600h100v100h-100zM1800 2600h100v100h-100zM1900 2600h100v100h-100zM0 2700h100v100H0z%22%2F%3E%3Cpath fill=%22%234c6e4723%22 d=%22M100 2700h100v100H100z%22%2F%3E%3Cpath fill=%22%234c6e47e5%22 d=%22M200 2700h100v100H200z%22%2F%3E%3Cpath fill=%22%234c6e479e%22 d=%22M300 2700h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e4765%22 d=%22M400 2700h100v100H400z%22%2F%3E%3Cpath fill=%22none%22 d=%22M500 2700h100v100H500zM600 2700h100v100H600zM700 2700h100v100H700zM800 2700h100v100H800zM900 2700h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e4745%22 d=%22M1000 2700h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1100 2700h100v100h-100zM1200 2700h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47b7%22 d=%22M1300 2700h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1400 2700h100v100h-100zM1500 2700h100v100h-100zM1600 2700h100v100h-100zM1700 2700h100v100h-100zM1800 2700h100v100h-100zM1900 2700h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e479d%22 d=%22M0 2800h100v100H0z%22%2F%3E%3Cpath fill=%22none%22 d=%22M100 2800h100v100H100zM200 2800h100v100H200zM300 2800h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e47de%22 d=%22M400 2800h100v100H400z%22%2F%3E%3Cpath fill=%22none%22 d=%22M500 2800h100v100H500z%22%2F%3E%3Cpath fill=%22%234c6e4797%22 d=%22M600 2800h100v100H600z%22%2F%3E%3Cpath fill=%22none%22 d=%22M700 2800h100v100H700zM800 2800h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e47ef%22 d=%22M900 2800h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e4713%22 d=%22M1000 2800h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e479f%22 d=%22M1100 2800h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1200 2800h100v100h-100zM1300 2800h100v100h-100zM1400 2800h100v100h-100zM1500 2800h100v100h-100zM1600 2800h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4754%22 d=%22M1700 2800h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1800 2800h100v100h-100zM1900 2800h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e477a%22 d=%22M0 2900h100v100H0z%22%2F%3E%3Cpath fill=%22none%22 d=%22M100 2900h100v100H100zM200 2900h100v100H200z%22%2F%3E%3Cpath fill=%22%234c6e47bf%22 d=%22M300 2900h100v100H300z%22%2F%3E%3Cpath fill=%22%234c6e47ed%22 d=%22M400 2900h100v100H400z%22%2F%3E%3Cpath fill=%22%234c6e4797%22 d=%22M500 2900h100v100H500z%22%2F%3E%3Cpath fill=%22none%22 d=%22M600 2900h100v100H600z%22%2F%3E%3Cpath fill=%22%234c6e4737%22 d=%22M700 2900h100v100H700z%22%2F%3E%3Cpath fill=%22%234c6e4772%22 d=%22M800 2900h100v100H800z%22%2F%3E%3Cpath fill=%22%234c6e47be%22 d=%22M900 2900h100v100H900z%22%2F%3E%3Cpath fill=%22%234c6e479c%22 d=%22M1000 2900h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1100 2900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4713%22 d=%22M1200 2900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4762%22 d=%22M1300 2900h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1400 2900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e4764%22 d=%22M1500 2900h100v100h-100z%22%2F%3E%3Cpath fill=%22%234c6e47e1%22 d=%22M1600 2900h100v100h-100z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1700 2900h100v100h-100zM1800 2900h100v100h-100zM1900 2900h100v100h-100z%22%2F%3E%3C%2Fg%3E%3Cdefs%3E%3CradialGradient id=%22a%22%3E%3Cstop offset=%220%22 stop-color=%22%23fff%22%2F%3E%3Cstop offset=%221%22 stop-color=%22%23fff%22 stop-opacity=%220%22%2F%3E%3C%2FradialGradient%3E%3C%2Fdefs%3E%3C%2Fsvg%3E");

'''
}
st.markdown(bg, unsafe_allow_html=True)

long_text = "Hello, this is the experiMENTAL health chatbot ui."

# Wrap the text to a specified width
wrapped_text = textwrap.fill(long_text, width=10)

#Add wrapped text to the sidebar
with st.sidebar:
   st.header("About the Project")
   st.write(wrapped_text)
   
openai.api_key = st.secrets["OPENAI_API_KEY"]


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

system_message = {
    "role": "system",
    "content": "You are a helpful AI Assistant that gives mental health advice and answers any questions the user might have. If the user says anything suicidal or homicidal reply with the word 'WARNING'"
}

st.session_state.messages.append(system_message)

for message in st.session_state.messages:
   if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})


