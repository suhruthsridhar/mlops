SELECT
    s.department AS Department,
    COUNT(DISTINCT s.student_id) AS Total_Students,
    COUNT(DISTINCT e.employee_id) AS Current_Mentors,
    SUM(DISTINCT e.mentor_capacity) AS Total_Capacity,
    SUM(s.fee) AS Total_Revenue,
    SUM(DISTINCT e.salary) AS Total_Cost,
    -- Calculate profit or loss (Revenue - Cost)
    (SUM(s.fee) - SUM(DISTINCT e.salar