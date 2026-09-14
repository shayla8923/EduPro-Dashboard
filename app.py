import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EduPro Dashboard", layout="wide")

import streamlit as st

st.set_page_config(
    page_title="EduPro Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 EduPro Learner Demographics & Course Enrollment Dashboard")
st.markdown("""
<h1 style='text-align:center; color:#1E88E5;'>
📊 EduPro Learner Analytics Dashboard
</h1>

<h4 style='text-align:center; color:gray;'>
Learner Demographics & Course Enrollment Analysis
</h4>
""", unsafe_allow_html=True)

st.divider()

df = pd.read_csv("C:/Edu Pro project/Notebooks/Merged_EduPro_Dataset.csv")

st.sidebar.header("Filters")

gender = st.sidebar.multiselect(
    "Gender_x",
    df["Gender_x"].unique(),
    default=df["Gender_x"].unique()
)

category = st.sidebar.multiselect(
    "Course Category",
    df["CourseCategory"].unique(),
    default=df["CourseCategory"].unique()
)

level = st.sidebar.multiselect(
    "Course Level",
    df["CourseLevel"].unique(),
    default=df["CourseLevel"].unique()
)

filtered_df = df[
    (df["Gender_x"].isin(gender)) &
    (df["CourseCategory"].isin(category)) &
    (df["CourseLevel"].isin(level))
]

st.header("👨‍🎓 Learner Demographic Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Learners", filtered_df["UserID"].nunique())
col2.metric("Average Age", round(filtered_df["Age_x"].mean(), 1))
col3.metric("Average Course Rating", round(filtered_df["CourseRating"].mean(), 2))

st.header("📊 Age-wise Enrollment")

fig, ax = plt.subplots(figsize=(8,4))

sns.histplot(filtered_df["Age_x"], bins=10, kde=True, ax=ax)

ax.set_xlabel("Age_x")
ax.set_ylabel("Number of Learners")

st.pyplot(fig)

st.header("👩‍🎓 Gender-based Course Preference")

gender_course = pd.crosstab(
    filtered_df["Gender_x"],
    filtered_df["CourseCategory"]
)

st.dataframe(gender_course)

fig, ax = plt.subplots(figsize=(8,5))
gender_course.plot(kind="bar", ax=ax)

plt.xticks(rotation=0)
plt.ylabel("Enrollments")

st.pyplot(fig)


st.header("📚 Course Category Popularity")

course_count = df["CourseCategory"].value_counts()

st.dataframe(course_count)

fig, ax = plt.subplots(figsize=(8,5))

course_count.plot(kind="bar", ax=ax)

plt.xticks(rotation=45)
plt.ylabel("Number of Enrollments")

st.pyplot(fig)

st.header("🎓 Course Level Distribution")

level_count = df["CourseLevel"].value_counts()

st.dataframe(level_count)

fig, ax = plt.subplots(figsize=(8,5))

level_count.plot(kind="bar", ax=ax)

plt.xticks(rotation=0)

st.pyplot(fig)


st.header("⭐ Average Course Rating")

rating = df.groupby("CourseCategory")["CourseRating"].mean()

st.dataframe(rating)

fig, ax = plt.subplots(figsize=(8,5))

rating.plot(kind="bar", ax=ax)

plt.xticks(rotation=45)

st.pyplot(fig)


st.header("💰 Course Price Distribution")

fig, ax = plt.subplots(figsize=(8,5))

ax.hist(df["CoursePrice"], bins=10)

plt.xlabel("Price")
plt.ylabel("Frequency")

st.pyplot(fig)


st.header("⏳ Course Duration")

duration = df.groupby("CourseCategory")["CourseDuration"].mean()

st.dataframe(duration)

fig, ax = plt.subplots(figsize=(8,5))

duration.plot(kind="bar", ax=ax)

plt.xticks(rotation=45)

st.pyplot(fig)

total_learners = df["UserID"].nunique()
total_courses = df["CourseID"].nunique()
total_revenue = df["Amount"].sum()
avg_rating = round(df["CourseRating"].mean(), 2)

col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Learners", total_learners)
col2.metric("📚 Courses", total_courses)
col3.metric("💰 Revenue", f"₹{total_revenue:,.0f}")
col4.metric("⭐ Avg Rating", avg_rating)


# with st.container():
#     st.subheader("📈 Age-wise Enrollment")


course_count.plot(
    kind="bar",
    color="mediumseagreen",
    ax=ax
)


st.divider()

st.sidebar.title("🎛 Dashboard Filters")

st.divider()

st.info("""
📌 This dashboard analyzes learner demographics,
course enrollment trends,
course popularity,
and learner preferences.
""")

left,right = st.columns(2)
