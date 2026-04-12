import qrcode
import os

riddles = [
    {
        "location": "Library",
        "text": "I have many leaves, but I am no tree. I have many stories, but I cannot speak. People come to me when they need quiet and knowledge. Where am I?"
    },
    {
        "location": "Engineering_Coordination",
        "text": "This is where logic meets design, and builders of the future align their plans. Whether it is for systems, code, or machines, you come here to organize your academic routines. Where am I?"
    },
    {
        "location": "Cashiers_Office",
        "text": "I am the place where your coins say goodbye, so your education can fly high. You visit me to settle your debt, making sure your semester is perfectly set. Where am I?"
    },
    {
        "location": "Dentistry_Clinic",
        "text": "I am a room full of crowns, but there are no kings. I have special chairs and bright lights that gleam. Open wide and show your smile, you might be sitting here for a while. Where am I?"
    }
]

output_dir = "riddle_qrs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

qr_config = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10, 
    border=4, 
)

for riddle in riddles:
    qr_config.add_data(riddle["text"])
    qr_config.make(fit=True)

    qr_image = qr_config.make_image(fill_color="black", back_color="white")

    file_name = f"{riddle['location']}_riddle_qr.png"
    file_path = os.path.join(output_dir, file_name)

    qr_image.save(file_path)

    qr_config.clear()

    print(f"Generated QR code for {riddle['location']} at: {file_path}")

print(f"\nSuccessfully generated {len(riddles)} QR codes in the '{output_dir}' directory.")