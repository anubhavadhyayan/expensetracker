-- Create expenses table
CREATE TABLE IF NOT EXISTS expenses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    amount DECIMAL(12, 2) NOT NULL,
    description TEXT,
    category TEXT DEFAULT 'General',
    date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Optional: Create an index on date for better performance
CREATE INDEX IF NOT EXISTS idx_expenses_date ON expenses(date);
