import pandas as pd

df = pd.read_csv(r"C:\Users\avivy\GitHub\Hacking 101\.CSV\Paths.csv", header=None)
A_col = df.iloc[:, 0].values
for i in range(186):
    print("start " + a + str(i) + "\n" + "timeout /t 5")
