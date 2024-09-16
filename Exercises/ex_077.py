listing = (
    'Learn', 'Innovate', 'Grow', 'Create', 'Explore', 'Discover', 'Analyze',
    'Build', 'Design', 'Develop', 'Implement', 'Test', 'Evaluate', 'Integrate',
    'Optimize', 'Solve', 'Collaborate', 'Plan', 'Code', 'Debug', 'Maintain',
)

vowels = 'aeiouAEIOU'

for c in listing:
    print(f'\nIn the word {c} we have:', end='')
    for char in c:
        if char in vowels:
            print(char.lower() + ' ', end='')
