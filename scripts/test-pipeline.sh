#!/bin/bash
echo "🧪 Testing Healthcare ETL Pipeline..."

# Create test file
cat > test.csv << 'EOF'
visit_id,patient_id,doctor_id,visit_date,treatment_cost
TEST001,P5001,D201,2024-04-01,2600
TEST002,P5002,D202,2024-04-01,1900
