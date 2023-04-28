"""BrickBridge"""
def main():
    """BrickBridge"""
    srock = int(input())
    mrock = int(input())
    goal = int(input())
    mrock_lm = goal//5
    if mrock > mrock_lm:
        mrock = mrock_lm
    goal = goal - (mrock*5)
    if goal > srock:
        print("-1")
    else:
        print(goal)
main()
