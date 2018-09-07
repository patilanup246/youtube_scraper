﻿destination = "D:\\aaron\\Videos\\YouTube"
num_videos = 50
delta = 24 * 60 * 60 * 7
channels = [
		{"channel": "100SekundenPhysik", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCEJDM_70A2EiRqZ41l6bZlg"},
		{"channel": "3Blue1Brown", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCYO_jab_esuFRV4b17AJtAw"},
		{"channel": "Aktien mit Kopf", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCpV9LpCg4uwYCQZ3qoEn_YQ"},
		{"channel": "Average Linux User", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCZiL6BoryLWxyapUuVYW27g"},
		{"channel": "blackpenredpen", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC_SvYP0k05UKiJ_2ndB02IA"},
		{"channel": "Break the Twitch", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCyicqwQM9aIZ9mAw5xP4Q2g"},
		{"channel": "Brotcrunsher", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC-3thK6H2pfxxGAa7qljipQ"},
		{"channel": "CaseyNeistat", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCtinbF-Q-fVthA0qrFQTgXQ"},
		{"channel": "Cg Kid", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCacn-Cy4KtIm-dl0iuLHAUA"},
		{"channel": "Charles Krüger", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCSLnD8xd-81Lc96OE9kBkOQ"},
		{"channel": "DeutscherHanfverband", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCNJxn7JS4saCHPsnD91yf9Q"},
		{"channel": "Dirk Kreuter", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCst-bv-rrm31AU27gNZ88qQ"},
		{"channel": "Drug Education Agency", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCFmLi6X1mojkFZOFngNR9tQ"},
                {"channel": "Eigthc", "url": "http://www.youtube.com/feeds/videos.xml?channel_id=UCP-ZCMz7olJPUI78b_bQrvQ"},
		{"channel": "Flammable Maths", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCtAIs1VCQrymlAnw3mGonhw"},
		{"channel": "Fratm", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCfXpCALnoC2zsdcKx2XirbQ"},
		{"channel": "Freedom in Thought", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCd6Za0CXVldhY8fK8eYoIuw"},
		{"channel": "Glücksdetektiv", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCtyU6E_Cbpd0k7Anta-ut5Q"},
		{"channel": "Green Rabbit / Philosophie, Psychologie, Existenz", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCbLBFACJUmyDSaouN9ucnnA"},
		{"channel": "Hello World", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCFZ-TZHiOgTg-BPbJDgI7zw"},
		{"channel": "Homo Oeconomicus", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC3vSoA532bQwBBKuJI9CjzQ"},
		{"channel": "Horst Lüning", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC5i6nCpwmDVKo98sZD2AAcQ"},
		{"channel": "JP Performance", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC1-VOKyTJrgLiBeiJqzeIUQ"},
		{"channel": "Kolja Barghoorn", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC1XJvortM-4D8ZRXYXd2T6A"},
		{"channel": "Kolja investiert", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCM_VUg9JdtfKKPBVyxqrgcQ"},
		{"channel": "Kris Occhipinti", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCf93fPKwotph47H3_KDcRyg"},
		{"channel": "LAHWF", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCQlVOYJyQp64rA12ac0mv6g"},
		{"channel": "LiveOverflow", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UClcE-kVhqyiHCcjYwcpfj9w"},
		{"channel": "Luke Smith", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC2eYFnH61tmytImy1mTYvhA"},
		{"channel": "Malte Helmhold", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCtLLr2p5ZsKTppwE9ctVO5A"},
		{"channel": "Mic. the Vegan", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCGJq0eQZoFSwgcqgxIE9MHw"},
		{"channel": "My Self Reliance", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCIMXKin1fXXCeq2UJePJEog"},
		{"channel": "Numberphile", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCoxcjq-8xIDTYp3uz647V5A"},
		{"channel": "Oliver Flesch", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCYo2MjFS5C7Wynyty9wTM7g"},
		{"channel": "Oliver Janich", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC3cmEfpy4XED7YYEe69nIMA"},
		{"channel": "OPEN MIND", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCEtYtMoD26j2BJBJ4w_hM6w"},
		{"channel": "OPEN MIND Reloaded", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCLr3ZCYkC8J2lMOFdET8mbA"},
		{"channel": "Peter Frahm Coaching", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCwV0CAC1UW1FMGo8-Pc1azw"},
		{"channel": "PsychedSubstance", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCn8V3KNSgDr1Dai77_y8JrQ"},
		{"channel": "RedeFabrik - Kommunikation &amp; Charisma", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCkC-9P-VbzSNzsgMwtGdOXg"},
		{"channel": "SemperVideo", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCCI6C8hD-hTZi2JEmS7zvQw"},
		{"channel": "sentdex", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCfzlCWGWYyIQ0aLC5w48gBQ"},
		{"channel": "Simon Clark", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCRRr_xrOm66qaigIbwFLvbQ"},
		{"channel": "Steuern mit Kopf", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCCwCa-faBqcY-zJ4PS1lCHA"},
		{"channel": "SWIM", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCOWGNAei4hIjOna_JgWGCOA"},
		{"channel": "TechGumbo", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCaSM4GqhbaVmRT7fmmFmR1w"},
		{"channel": "The Morpheus Tutorials", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCLGY6_j7kZfA1dmmjR1J_7w"},
		{"channel": "TheRaRaRabbit", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCjiSE1TQ6864azsWP9hEelA"},
		{"channel": "TrauKeinemPromi", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCWidwHMq-wJJOQ4ESNo-RdA"},
		{"channel": "tripcode!Q/7", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCZrrEuHiQjN2CUo84g5tk7w"},
		{"channel": "tutoriaLinux", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCvA_wgsX6eFAOXI8Rbg_WiQ"},
		{"channel": "unicks.eu", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCnZIn_CYjz0ErPs1ktH-2lQ"},
		{"channel": "Valentin Möller", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCyHK70XuRaWjwBnz2jHWxeg"},
		{"channel": "Versicherungen mit Kopf", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC70-qPE5cS_aOYAOGnM_24g"},
		{"channel": "Weitz / HAW Hamburg", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCjTfChr0yyz4iZq0x12Q6xA"},
		{"channel": "What I've Learned", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCqYPhGiB9tkShZorfgcL2lA"},
		{"channel": "Word Porn", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCbiS-tMYNTIUv1y6uVh27Zw"},
		{"channel": "Your Mate Tom", "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCXSF1F_RFRUVNXX4QmB6vmw"}]
