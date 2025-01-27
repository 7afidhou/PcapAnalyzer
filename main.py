import os
from flask import Flask, render_template, request
from scapy.all import rdpcap, IP
from collections import Counter

app = Flask(__name__)

def analyze_pcap(file_path, threshold=100):
    packets = rdpcap(file_path)
    ip_counter = Counter()
    dest_ip_counter = Counter()

    for packet in packets:
        if IP in packet:
            ip_counter[packet[IP].src] += 1
            dest_ip_counter[packet[IP].dst] += 1

    top_sources = ip_counter.most_common(5)
    top_destinations = dest_ip_counter.most_common(5)
    potential_ddos_sources = [(ip, count) for ip, count in ip_counter.items() if count > threshold]
    potential_ddos_targets = [(ip, count) for ip, count in dest_ip_counter.items() if count > threshold]

    return {
        "total_packets": len(packets),
        "top_sources": top_sources,
        "top_destinations": top_destinations,
        "potential_ddos_sources": potential_ddos_sources,
        "potential_ddos_targets": potential_ddos_targets,
    }

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        pcap_file = request.files["pcap_file"]
        threshold = int(request.form.get("threshold", 100))
        if pcap_file:
            file_path = f"./{pcap_file.filename}"
            pcap_file.save(file_path)
            results = analyze_pcap(file_path, threshold)
            
            # Delete the file after analyzing
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting file: {e}")
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
