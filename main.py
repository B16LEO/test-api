import requests
import base64

# --- DATA DARI AKUNMU ---
USER_ID = "V1:dikcqbolh0p3jkqq:DEVCENTER:EXT"
PASSWORD = "J99emFxI"
# Ganti URL ini jika kamu tahu alamat API aslinya
BASE_URL = "https://api.test.sabre.com" 

def sambungkan():
    print("Mencoba menghubungkan...")
    
    # Gabungkan User ID & Pass untuk otentikasi
    auth_str = f"{USER_ID}:{PASSWORD}"
    encoded_auth = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    try:
        # Tahap 1: Ambil Token
        res = requests.post(f"{BASE_URL}/v2/auth/token", 
                            headers=headers, 
                            data={"grant_type": "client_credentials"})
        
        if res.status_code == 200:
            token = res.json().get('access_token')
            print("✅ BERHASIL!")
            print(f"Token kamu: {token[:20]}...") 
        else:
            print(f"❌ GAGAL: {res.status_code}")
            print(res.text)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    sambungkan()
