import numpy as np
import matplotlib.pyplot as plt

# กำหนดชุดของความเร็ว
velocity = np.arange(0, 101, 1)

# กำหนดฟังก์ชันการสูงส่ง (Membership Functions)
def slow_membership(velocity):
    if 0 <= velocity < 30:
        return 1
    elif 30 <= velocity < 60:
        return (60 - velocity) / 30
    else:
        return 0

def medium_membership(velocity):
    if 30 <= velocity < 60:
        return (velocity - 30) / 30
    elif 60 <= velocity < 90:
        return (90 - velocity) / 30
    else:
        return 0

def fast_membership(velocity):
    if 60 <= velocity < 90:
        return (velocity - 60) / 30
    elif 90 <= velocity <= 100:
        return 1
    else:
        return 0

# กำหนดกฎ IF-THEN อีก 9 กฎ
def control_rule(velocity):
    if slow_membership(velocity) > 0.5:
        # กระทำเมื่อความเร็วช้า
        return "slow_down"
    elif medium_membership(velocity) > 0.5:
        # กระทำเมื่อความเร็วปานกลาง
        return "maintain_speed"
    elif fast_membership(velocity) > 0.5:
        # กระทำเมื่อความเร็วเร็ว
        return "speed_up"
    elif 10 <= velocity < 40:
        return "slow_down"
    elif 40 <= velocity < 70:
        return "maintain_speed"
    elif 70 <= velocity < 100:
        return "speed_up"
    elif 20 <= velocity < 50:
        return "slow_down"
    elif 50 <= velocity < 80:
        return "maintain_speed"
    elif 80 <= velocity < 95:
        return "speed_up"
    else:
        return "do_nothing"

# แสดงฟังก์ชันการสูงส่งบนกราฟ
plt.plot(velocity, [slow_membership(v) for v in velocity], label='Slow')
plt.plot(velocity, [medium_membership(v) for v in velocity], label='Medium')
plt.plot(velocity, [fast_membership(v) for v in velocity], label='Fast')

plt.title('Membership Functions for Velocity')
plt.xlabel('Velocity (mph)')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid(True)
plt.show()

# ตัวอย่างการใช้กฎในการควบคุมความเร็ว
current_velocity = 55  # ความเร็วปัจจุบัน
action = control_rule(current_velocity)
print(f"Current velocity: {current_velocity} mph, Action: {action}")
