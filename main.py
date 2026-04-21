import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from pyscript import document

# rthbis resets the data
absences_data = {
    'Monday': 0, 
    'Tuesday': 0, 
    'Wednesday': 0, 
    'Thursday': 0, 
    'Friday': 0
}

def handle_submit(event):
    # 
    day = document.querySelector("#daySelect").value
    raw_value = document.querySelector("#absenceInput").value
    
    # this coverts the number into intgere
    try:
        num_absences = int(raw_value) if raw_value else 0
    except ValueError:
        num_absences = 0

    # this updates the graph
    absences_data[day] = num_absences
    
    # this generates the graph
    days = list(absences_data.keys())
    counts = list(absences_data.values())
    
    #small help from ai -- i asked help where to put which
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(days, counts, marker='o', color='#198754', linewidth=2, markersize=8)
    ax.set_title('Weekly Absence Trend', fontsize=14, pad=15)
    ax.set_ylabel('Number of Students')
    ax.set_ylim(bottom=0) # Ensure Y axis starts at 0
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # small help aswell -- i just asked how to close this python code
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    
    # 5. Push the image back to the HTML container
    img_tag = f'<img src="data:image/png;base64,{img_base64}"/>'
    document.querySelector("#graph-output").innerHTML = img_tag
