# pip install speedtest-cli
import speedtest

def test_internet_speed():
    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Get the download and upload speeds
    download_speed = st.download()
    upload_speed = st.upload()
    
    # Convert the speeds to megabits per second (Mbps)
    download_speed_mbps =  download_speed / 1000000
    upload_speed_mbps = upload_speed / 1000000
    
    print(f"Download speed: {download_speed_mbps: 2f} Mbps")
    print(f"Upload speed: {upload_speed_mbps: 2f} Mbps")
    
# Example usage
test_internet_speed()