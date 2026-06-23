import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file = pd.read_csv("D:\\Sai Jyothi\\Anudip Foundation\\Major_Project\\DataSet.csv",encoding='latin1')
print(file.head)
#checking any duplicates are present in the file
num_duplicate_rows = (file.duplicated().sum())
print(f"Number of duplicate rows: {num_duplicate_rows}")
#checking any null values are present in the file
total_missing_values = file.isnull().sum().sum()
print(f"\nTotal number of missing values in the dataset: {total_missing_values}")
file['AI_Impact_Score'] = (
    file['AI_Exposure_Index'] * 0.4 +
    file['Automation_Probability_2030'] * 0.4 +
    file['Tech_Growth_Factor'] * 0.2
)
# 4. Find the Job Most Affected by AI
unique_jobs = file.sort_values(by='AI_Impact_Score', ascending=False) \
                .drop_duplicates(subset=['Job_Title'], keep='first')
# 5. Get the Most AI-Affected Unique Job
top_unique_job = unique_jobs[['Job_Title', 'AI_Impact_Score']].head(10)
# 6. Print the result
print("MOST AI-AFFECTED UNIQUE JOB ROLE:")
print(top_unique_job)
job_name = top_unique_job.iloc[0]['Job_Title']
impact = top_unique_job.iloc[0]['AI_Impact_Score']
print("\n Top one effected job is:", job_name)
print("Impact Score:", round(impact, 4))
#what jobs will be most effected by 2030?
job= unique_jobs[['Job_Title','AI_Impact_Score']].tail()
print("Lowest AI Impact jobs is:")
print(job)

#PRINT THE PIECHART
risk_col = None
for c in file.columns:
    if "risk" in c.lower() or "category" in c.lower():
        risk_col = c
        break
# If no risk column found, create a placeholder
if risk_col is None:
    raise ValueError("No Risk Category column found in dataset. Please specify the column name.")
# Calculate percentage distribution
risk_counts = file[risk_col].value_counts(dropna=False)
risk_percent = (risk_counts / len(file)) * 100
# Plot pie chart
plt.figure(figsize=(6,6))
plt.pie(risk_percent, labels=risk_percent.index, autopct='%1.1f%%')
plt.title("Percentage of Jobs by Risk Category")
plt.show()


#Relationship between AI IMPACT SCORE VS AUTOMATION PROBABILITY USING SCATTER PLOT
aI_exposure_index=file['AI_Impact_Score']
automation_probability_2030=file['Automation_Probability_2030']
plt.scatter(aI_exposure_index,automation_probability_2030)
plt.xlabel('AI IMPACT SCORE')
plt.ylabel('AUTOMATION PROBABILITY')
plt.title('RELATIONSHIP BETWEEN AI IMPACT SCORE VS AUTOMATION PROBABILITY')
plt.show()
impact_col = "AI_Exposure_Index"

#SKILLS VS AVERAGE AI IMPACT USING BARCHARTS
# Identify all skill columns (Skill_1, Skill_2, ..., Skill_10)
skill_cols = [c for c in file.columns if "skill" in c.lower()]

# Dictionary to store average impact per skill
skill_impact = {}

# Loop through each skill column
for col in skill_cols:
    for skill in file[col].dropna().unique():
        # Find rows where the skill appears in ANY skill column
        mask = (file[skill_cols] == skill).any(axis=1)
        avg_val = file.loc[mask, impact_col].mean()
        skill_impact[skill] = avg_val

# Convert results to DataFrame
skill_file = pd.DataFrame({
    "Skill": list(skill_impact.keys()),
    "Average_AI_Impact": list(skill_impact.values())
})

# Sort and select top 15 skills
skill_file = skill_file.sort_values("Average_AI_Impact", ascending=False).head(15)

# Plot bar chart
plt.figure(figsize=(12,6))
plt.bar(skill_file["Skill"], skill_file["Average_AI_Impact"])
plt.xticks(rotation=90)
plt.title("Skill Levels vs Average AI Impact")
plt.xlabel("Skill")
plt.ylabel("Average AI Impact")
plt.tight_layout()
plt.show()







