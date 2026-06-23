📌 Project Overview

This project analyzes the impact of Artificial Intelligence (AI) on various job roles by the year 2030. Using a dataset of **3,000 job records across 18 attributes**, we compute an **AI Impact Score** for each job role, rank the most and least affected occupations, and visualize the findings through insightful charts.

The goal is to help job seekers, students, researchers, and policymakers understand which roles are most vulnerable to AI automation — and which are safest.

🗂️ Project Structure

AI-Impact-on-Jobs-2030/

│
├── DataSet.csv
├── main.py
├── README.md
├── requirements.txt
├── outputs
│   ├── pie_chart.png
│   ├── scatter_plot.png
│   └── bar_chart.png
└── docs/
└── architecture.png

📊 Dataset Description

| Column | Description |
|--------|-------------|
| `Job_Title` | Name of the job role |

| `AI_Exposure_Index` | How exposed the job is to AI |

| `Automation_Probability_2030` | Likelihood of automation by 2030 |

| `Tech_Growth_Factor` | Influence of tech growth on the role |

| `Skill_1` to `Skill_10` | Skills associated with the role |

| `Risk_Category` | High / Medium / Low classification |

⚙️ Methodology

AI Impact Score Formula

AI_Impact_Score = (AI_Exposure_Index × 0.4)+ (Automation_Probability_2030 × 0.4)+ (Tech_Growth_Factor × 0.2)

🔍 Key Findings
| Finding | Detail |
|---------|--------|
| 🔴 Most at-risk | Customer Support (Score: 1.06) |

| 🔴 2nd most at-risk | Retail Worker |

| 🔴 3rd most at-risk | Truck Driver |

| 🟢 Safest job | Doctor |

| 🟢 2nd safest | Nurse |

| 🟢 3rd safest | Teacher |

| 📊 Risk split | Medium 50.7% · High 24.7% · Low 24.6% |

🚀 How to Run

```bash
git clone https://github.com/yourusername/AI-Impact-on-Jobs-2030.git

cd AI-Impact-on-Jobs-2030

pip install -r requirements.txt

python main.py

```
🛠️ Tech Stack

| Tool | Purpose |

|------|---------|

| Python 3.9 | Core language |

| Pandas | Data manipulation |

| NumPy | Numerical computation |

| Matplotlib | Visualization |

🔮 Future Enhancements
ML classifier to predict job risk category| Power BI enterprise reporting|Country/region-wise analysis

👤 Author

Sai Jyothi

GitHub:saijyothi-18|https://github.com/saijyothi-18

LinkedIn:Paradesi Saijyothi|https://www.linkedin.com/in/paradesi-saijyothi-7699782a7/

⭐ If you found this helpful, give it a star on GitHub!
