s=input()
n=s.split(":")
m_hand=int(n[1])*6
h_hand=(int(n[0])%12 + int(n[1])/60)*30
print(min(abs(m_hand-h_hand),360-(abs(m_hand-h_hand))))