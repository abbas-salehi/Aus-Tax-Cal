
import streamlit as st

st.set_page_config(page_title="🇦🇺 Australian Tax Calculator", layout="centered")

st.title("🇦🇺 Australian Tax Calculator 2024–25")
st.subheader("Estimate your income tax and refund (or amount owed) in seconds.")

# Inputs
income = st.number_input("Annual Taxable Income ($)", min_value=0, step=1000, value=70000)
withheld = st.number_input("Tax Withheld by Employer ($)", min_value=0, step=500, value=14000)

st.markdown("#### 🧮 Tax Calculation")

# Basic 2024–25 Australian resident tax brackets (simplified, no offsets/deductions)
def calculate_tax(income):
    if income <= 18200:
        return 0
    elif income <= 45000:
        return (income - 18200) * 0.19
    elif income <= 135000:
        return 5092 + (income - 45000) * 0.30
    elif income <= 190000:
        return 29467 + (income - 135000) * 0.37
    else:
        return 49717 + (income - 190000) * 0.45

tax_payable = calculate_tax(income)
difference = withheld - tax_payable

# Results
st.write(f"**🧾 Estimated Tax Payable:** ${tax_payable:,.2f}")
if difference > 0:
    st.success(f"✅ Estimated Tax Refund: ${difference:,.2f}")
elif difference < 0:
    st.error(f"❌ You may owe: ${-difference:,.2f}")
else:
    st.info("😐 Your tax is perfectly balanced.")

# Footer
st.markdown("---")
st.markdown("This calculator is a simple estimate and does not account for deductions, offsets, or Medicare levy.")


st.markdown("---")
st.markdown("📄 **Bonus PDF:** [Download '5 Ways to Maximise Your Aussie Tax Refund'](https://drive.google.com/file/d/1k07cVTlW1fl7f58VtmYZkItPkueaF480/view?usp=drive_link)")

