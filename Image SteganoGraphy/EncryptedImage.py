from stegano import lsb

encrypted_image=lsb.hide("leetcode.png",'LeetCode is Fun!!')
encrypted_image.save("Encrypted_Leetcode.png")