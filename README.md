# PCAP Analyzer with DDoS Detection

This is a Flask-based web application for analyzing PCAP (Packet Capture) files. The application detects potential DDoS attacks by identifying unusual traffic patterns and displays the results in a clean, Bootstrap-styled interface.

## Features

- Upload a PCAP file for analysis.
- Detect top source and destination IPs.
- Identify potential DDoS sources and targets based on a configurable traffic threshold.
- Automatically deletes the uploaded file after analysis.
- Responsive UI styled with Bootstrap.

## Prerequisites

Before running the application, ensure the following are installed:

- Python 3.8 or later
- Required Python libraries:
  - `Flask`
  - `Scapy`

## Installation

1. **Clone or download the repository**:
   ```bash
   git clone https://github.com/7afidhou/PcapAnalyzer.git
   cd PcapAnalyzer
