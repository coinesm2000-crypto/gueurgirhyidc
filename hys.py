import requests
import os

# List of URLs containing configs
urls = [
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt"
]

# The output file will be saved in the root of the project
output_file_path = 'stream_data.txt'

def main():
    """
    Main function to download, filter, and save configs for GitHub Actions.
    """
    print("Fetching configs from servers...")
    all_hysteria2_configs = []
    
    for url in urls:
        try:
            print(f"Fetching from: {url}")
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            
            source_lines = response.text.splitlines()
            hysteria2_from_source = [line for line in source_lines if line.strip().startswith('hysteria2://')]
            
            count = len(hysteria2_from_source)
            print(f"Found {count} hysteria2 configs from this source.")
            
            all_hysteria2_configs.extend(hysteria2_from_source)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching from {url}: {e}")
            continue

    if not all_hysteria2_configs:
        print("No hysteria2 configs were found from any source. Exiting.")
        return

    try:
        configs_text = "\n".join(all_hysteria2_configs)
        
        total_count = len(all_hysteria2_configs)
        print(f"\nSaving a total of {total_count} configs to file...")
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(configs_text)
        print(f"✅ Configs saved successfully to: {output_file_path}")

    except Exception as e:
        print(f"An unexpected error occurred while saving the file: {e}")

if __name__ == "__main__":
    main()
