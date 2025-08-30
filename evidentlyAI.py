import pandas as pd
from sklearn.datasets import load_iris
from evidently.core.report import Report
from evidently.presets import DataDriftPreset
import evidently
print(evidently.__version__, " - evidently version")


# Load training (baseline) and production data
iris = load_iris(as_frame=True)
ref_data = iris.frame.sample(frac=0.7, random_state=1)   # training
prod_data = iris.frame.sample(frac=0.3, random_state=2)  # new data

# Create a drift report
report = Report(metrics=[DataDriftPreset()])
# save report to html file
snap = report.run(reference_data=ref_data, current_data=prod_data)
snap.save_html("drift_report.html")


# Generate HTML report
# report.save_html("drift_report.html")
# report.show_html()
