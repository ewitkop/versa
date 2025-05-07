
 
import subprocess
import time
 
# Settings
base_ip = "10.10.50."      # Customize this based on your local subnet
start_ip = 105              # Starting IP offset
interface = "ens3"          # Change to match your interface name
num_ips = 100
 
 
 
websites = [
 "boston.com",
 "facebook.com",
 "google.com",
 "youtube.com",
 "instagram.com",
 "linkedin.com",
 "ajax.googleapis.com",
 "plus.google.com",
 "pinterest.com",
 "wordpress.org",
 "en.wikipedia.org",
 "youtu.be",
 "itunes.apple.com",
 "github.com",
 "bit.ly",
 "play.google.com",
 "goo.gl",
 "docs.google.com",
 "cdnjs.cloudflare.com",
 "vimeo.com",
 "support.google.com",
 "google-analytics.com",
 "maps.googleapis.com",
 "flickr.com",
 "medium.com",
 "sites.google.com",
 "drive.google.com",
 "creativecommons.org",
 "developers.google.com",
 "soundcloud.com",
 "theguardian.com",
 "apis.google.com",
 "chrome.google.com",
 "cloudflare.com",
 "nytimes.com",
 "maxcdn.bootstrapcdn.com",
 "support.microsoft.com",
 "blogger.com",
 "forbes.com",
 "s3.amazonaws.com",
 "code.jquery.com",
 "dropbox.com",
 "paypal.com",
 "apps.apple.com",
 "tinyurl.com",
 "theatlantic.com",
 "m.facebook.com",
 "archive.org",
 "cnn.com",
 "policies.google.com",
 "commons.wikimedia.org",
 "issuu.com",
 "wordpress.com",
 "wp.me",
 "businessinsider.com",
 "yelp.com",
 "mail.google.com",
 "support.apple.com",
 "apple.com",
 "bbc.com",
 "googleads.g.doubleclick.net",
 "mozilla.org",
 "eventbrite.com",
 "slideshare.net",
 "w3.org",
 "accounts.google.com",
 "messenger.com",
 "web.archive.org",
 "secure.gravatar.com",
 "usatoday.com",
 "huffingtonpost.com",
 "stackoverflow.com",
 "fb.com",
 "techcrunch.com",
 "wired.com",
 "eepurl.com",
 "arxiv.org",
 "finance.yahoo.com",
 "player.vimeo.com",
 "cnn.com",
 "yahoo.com",
 "developer.mozilla.org",
 "tumblr.com", ]
 
 
 
 
 
 
def add_virtual_ips():
    print("Adding virtual IPs...")
    for i in range(num_ips):
        ip = f"{base_ip}{start_ip + i}"
        cmd = ["sudo", "ip", "addr", "add", f"{ip}/24", "dev", interface]
        try:
            subprocess.run(cmd, check=True)
            print(f"Added {ip}")
        except subprocess.CalledProcessError:
            print(f"Failed to add {ip} (might already exist)")
 
def download_websites():
    print("Downloading websites...")
    for i, site in enumerate(websites):
        ip = f"{base_ip}{start_ip + (i % num_ips)}"
        cmd = ["wget", "--timeout=1",site, "--bind-address", ip, "-q", "-O", f"/dev/null"]
        print(f"URL No: {i}")
        try:
            subprocess.run(cmd, check=True)
            print(f"[{ip}] Fetched {site}")
        except subprocess.CalledProcessError:
            print(f"[{ip}] Failed to fetch {site}")
        time.sleep(1)  # Avoid hammering sites
 
if __name__ == "__main__":
    add_virtual_ips()
    download_websites()
