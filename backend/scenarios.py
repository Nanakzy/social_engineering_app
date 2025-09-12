# backend/scenarios.py

scenarios = [
    {
        "id": "usb_drop",
        "title": "USB Drop Attack",
        "frames": [
            "An employee finds a USB stick in the parking lot.",
            "They plug it into their work computer.",
            "Malware installs silently, giving hackers access.",
            "Lesson: Never use unknown devices."
        ],
        "background": None
    },
    {
        "id": "wifi_share",
        "title": "Wi-Fi Sharing Risk",
        "frames": [
            "A visitor asks for the company Wi-Fi password.",
            "The employee shares it without thinking.",
            "The visitor connects and sniffs company traffic.",
            "Lesson: Always use guest Wi-Fi for visitors."
        ],
        "background": None
    },
    {
        "id": "phishing_email",
        "title": "Phishing Email",
        "frames": [
            "An employee receives an urgent email from 'IT Support'.",
            "It asks them to click a link and reset their password.",
            "They enter credentials on a fake site.",
            "Lesson: Always verify suspicious emails before acting."
        ],
        "background": None
    },
    {
        "id": "password_sharing",
        "title": "Password Sharing",
        "frames": [
            "A colleague asks for your login to complete a task.",
            "You share your password thinking it’s harmless.",
            "The colleague accidentally exposes your credentials.",
            "Lesson: Never share passwords; use proper access control."
        ],
        "background": None
    },
    {
        "id": "sticky_note",
        "title": "Sticky Note Password",
        "frames": [
            "An employee writes their password on a sticky note.",
            "They leave it on their desk while away.",
            "Someone sees it and gains unauthorized access.",
            "Lesson: Never write passwords down; use a password manager."
        ],
        "background": None
    },
    {
        "id": "tailgating",
        "title": "Physical Tailgating",
        "frames": [
            "An unknown person follows employees into the office.",
            "No one checks their ID.",
            "They access restricted areas unnoticed.",
            "Lesson: Always verify identities before granting access."
        ],
        "background": None
    },
    {
        "id": "printer_data",
        "title": "Printer Confidentiality",
        "frames": [
            "Sensitive documents are printed and left on the printer.",
            "Anyone walking by can read or take them.",
            "Data is leaked without realizing.",
            "Lesson: Always collect and secure printed documents."
        ],
        "background": None
    },
    {
        "id": "personal_device",
        "title": "Unauthorized Personal Device",
        "frames": [
            "An employee connects a personal laptop to the office network.",
            "It contains malware unknowingly.",
            "The malware spreads across the corporate network.",
            "Lesson: Only use approved devices on company networks."
        ],
        "background": None
    },
    {
        "id": "social_media_leak",
        "title": "Social Media Overshare",
        "frames": [
            "An employee posts work schedule and projects online.",
            "A hacker gathers this info to craft a convincing scam.",
            "Company information is at risk.",
            "Lesson: Be careful about sharing work details publicly."
        ],
        "background": None
    },
    {
        "id": "weak_password",
        "title": "Weak Password Usage",
        "frames": [
            "An employee uses '123456' as their password.",
            "A hacker easily guesses it using common password lists.",
            "They gain access to sensitive accounts.",
            "Lesson: Always use strong, unique passwords."
        ],
        "background": None
    },
    {
        "id": "unverified_email_attachment",
        "title": "Unverified Email Attachment",
        "frames": [
            "An employee opens an attachment from an unknown sender.",
            "It installs ransomware on their computer.",
            "Files are encrypted and unavailable.",
            "Lesson: Never open attachments from unknown sources."
        ],
        "background": None
    },
    {
        "id": "shoulder_surfing",
        "title": "Shoulder Surfing",
        "frames": [
            "Someone looks over your shoulder while you enter a password.",
            "They capture your credentials without your knowledge.",
            "Lesson: Always shield sensitive information when typing."
        ],
        "background": None
    },
    {
        "id": "phoning_it",
        "title": "Fake IT Call",
        "frames": [
            "An employee receives a call claiming to be IT Support.",
            "They are asked for login credentials to 'fix an issue'.",
            "The employee provides access, unknowingly to a hacker.",
            "Lesson: Never give credentials over the phone; verify first."
        ],
        "background": None
    },
    {
        "id": "public_wifi",
        "title": "Using Public Wi-Fi",
        "frames": [
            "An employee connects to public Wi-Fi without a VPN.",
            "Sensitive company data is intercepted by attackers.",
            "Lesson: Always use secure connections when working remotely."
        ],
        "background": None
    },
    {
        "id": "reuse_password",
        "title": "Password Reuse",
        "frames": [
            "An employee uses the same password across multiple accounts.",
            "If one account is compromised, all others are at risk.",
            "Lesson: Use unique passwords for every account."
        ],
        "background": None
    },
    {
        "id": "discard_confidential",
        "title": "Improper Disposal of Documents",
        "frames": [
            "Confidential documents are thrown in regular trash.",
            "A passerby finds them and leaks sensitive data.",
            "Lesson: Always shred or securely dispose of confidential documents."
        ],
        "background": None
    },
    {
        "id": "unpatched_software",
        "title": "Ignoring Software Updates",
        "frames": [
            "An employee ignores software update notifications.",
            "Hackers exploit old vulnerabilities to gain access.",
            "Lesson: Always apply updates and patches promptly."
        ],
        "background": None
    },
    {
        "id": "left_computer_unlocked",
        "title": "Leaving Computer Unlocked",
        "frames": [
            "An employee leaves their computer unlocked while away.",
            "Someone else accesses sensitive files.",
            "Lesson: Lock your computer whenever unattended."
        ],
        "background": None
    },
    {
        "id": "shadow_it",
        "title": "Using Unauthorized Apps",
        "frames": [
            "Employees install unapproved apps for convenience.",
            "These apps contain security vulnerabilities.",
            "Lesson: Only use company-approved software."
        ],
        "background": None
    },
    {
        "id": "personal_email_for_work",
        "title": "Using Personal Email for Work",
        "frames": [
            "An employee sends company data through personal email.",
            "Data is exposed if personal account is hacked.",
            "Lesson: Always use official communication channels."
        ],
        "background": None
    },
    # Advanced / High-Risk Scenarios
    {
        "id": "tailored_phishing",
        "title": "Spear Phishing",
        "frames": [
            "An employee receives an email that looks like it’s from their manager.",
            "The email requests urgent action on a financial transaction.",
            "They comply without verifying, losing company funds or data.",
            "Lesson: Always verify unusual requests directly with the sender."
        ],
        "background": None
    },
    {
        "id": "impersonation_call",
        "title": "CEO/Executive Impersonation",
        "frames": [
            "An attacker calls pretending to be the CEO.",
            "They request sensitive files or urgent fund transfers.",
            "The employee complies, thinking it’s legitimate.",
            "Lesson: Always verify requests from executives through official channels."
        ],
        "background": None
    },
    {
        "id": "rogue_iot",
        "title": "Rogue IoT Device",
        "frames": [
            "An employee connects an unknown smart device to the network.",
            "The device is infected with malware, compromising internal systems.",
            "Lesson: Only connect authorized devices to the company network."
        ],
        "background": None
    },
    {
        "id": "dumpster_diving",
        "title": "Dumpster Diving",
        "frames": [
            "Sensitive documents are thrown in the trash without shredding.",
            "An outsider retrieves and exploits them for confidential info.",
            "Lesson: Always shred sensitive documents before disposal."
        ],
        "background": None
    },
    {
        "id": "remote_desktop_exploit",
        "title": "Remote Desktop Misuse",
        "frames": [
            "An employee enables remote access without IT approval.",
            "Hackers exploit the open connection to gain control of the system.",
            "Lesson: Only use remote access configured by IT."
        ],
        "background": None
    },
    {
        "id": "fake_social_profile",
        "title": "Fake Social Media Friend",
        "frames": [
            "An employee accepts a connection request from a fake profile.",
            "The attacker gains information to craft personalized scams.",
            "Lesson: Verify contacts and be cautious sharing work info online."
        ],
        "background": None
    },
    {
        "id": "rogue_app_store",
        "title": "Unverified App Download",
        "frames": [
            "An employee downloads a work-related app from an unofficial source.",
            "It contains malware that compromises corporate data.",
            "Lesson: Only download apps from trusted and approved sources."
        ],
        "background": None
    },
    {
        "id": "cloud_misconfiguration",
        "title": "Cloud Misconfiguration",
        "frames": [
            "An employee stores sensitive company files in a public cloud folder by mistake.",
            "Anyone on the internet can access the data.",
            "Lesson: Follow company policies for secure cloud storage."
        ],
        "background": None
    },
    {
        "id": "tailored_vishing",
        "title": "Vishing Attack",
        "frames": [
            "An employee receives a convincing phone call claiming to be a vendor.",
            "They provide account numbers and internal details over the phone.",
            "Lesson: Verify all requests via official communication channels."
        ],
        "background": None
    },
    {
        "id": "man_in_middle",
        "title": "Man-in-the-Middle Attack",
        "frames": [
            "An employee connects to an unsecured Wi-Fi hotspot at a café.",
            "Attackers intercept credentials and sensitive communications.",
            "Lesson: Use a secure VPN when accessing company resources on public networks."
        ],
        "background": None
    }
]

