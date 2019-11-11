def check_waist(people_pose):
    Neck = people_pose[2:4]
    RHeap,LHeap = people_pose[4:6],people_pose[10:12]

    MHeap = ((RHeap[0]+LHeap[0])/2, (RHeap[1]+LHeap[1])/2)
    
    if MHeap[0]!=Neck[0]:
        return True
    else:
        return False
        
def check_knee(people_pose):
    RKnee,RAnkle = people_pose[6:8],people_pose[8:10]
    LKnee,LAnkle = people_pose[12:14],people_pose[14:]
    
    # compare x point
    ChKnee = RKnee if RKnee[0]<LKnee[0] else LKnee
    ChAnkle = RAnkle if RAnkle[0]<LAnkle[0] else LAnkle
    
    if ChKnee[0] < ChAnkle[0]: 
        feedback_knee()
    
def feedback_waist():
    print("허리와 엉덩이를 일직선으로 맞춰주세요")
    
def feedback_knee():
    print("다리를 수직으로 맞춰주세요")