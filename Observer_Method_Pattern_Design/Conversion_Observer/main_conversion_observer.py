import meterobserver
import smoothobserver
import feetobserver
import measurement

def main():
    myMeas = measurement.Measurement()
    myFeet = feetobserver.FeetObserver(myMeas)
    myMetr = meterobserver.MeterObserver(myMeas)
    mySmooth = smoothobserver.SmoothObserver(myMeas)

    done = False
    while (not done):
        myVal = input("Enter the measure in inches (or Q to QUIT): ")
        if myVal == "Q":
            done = True
        else:
            myMeas.inches = float(myVal)
        print()

main()