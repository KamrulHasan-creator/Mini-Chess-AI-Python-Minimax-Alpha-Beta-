# Mini Chess (CLI) — একটি সিম্পল চেস প্রোজেক্ট

**বর্ণনা (বাংলা):**  
এই প্রোজেক্টটি একটি CLI (টার্মিনাল) ভিত্তিক চেস গেম যেখানে আপনি White হিসেবে খেলবেন এবং AI হলো Black। AI একটি সিম্পল **Minimax + Alpha-Beta** প্রুনিং ব্যবহার করে (উপরের কোডে depth দেওয়া আছে) এবং মূল্যায়ন হিসেবে শুধু পিস ভ্যালু ব্যবহার করে।

**ফাইলসমূহ:**  
- `main.py` — খেলার প্রধান লুপ ও ইউজার ইন্টারঅ্যাকশন।  
- `ai.py` — minimax + alpha-beta ও evaluation function।  
- `README.md` — এই ফাইল।

**প্রয়োজনীয়তা (Requirements):**  
- Python 3.8+  
- `python-chess` লাইব্রেরি (install করতে):
```bash
pip install python-chess
```

**কিভাবে চালাবেন:**  
```bash
python main.py
```
1. চালানোর সময় আপনাকে AI depth জিজ্ঞেস করবে (রেকমন্ডেড 2-4)।  
2. আপনি White হিসেবে খেলবেন; move দিন UCI ফরম্যাটে (উদাহরণ: `e2e4`, `g1f3`, `e7e8q` ইত্যাদি)।  
3. AI নিজে চাল দেবে।  
4. `quit` লিখলে প্রস্থান করা যাবে।

**নোটস:**  
- এই প্রোজেক্টটি শিক্ষামূলক উদ্দেশ্যে; AI খুব শক্তিশালী নয়।  
- উন্নত করতে পারেন: position evaluation improve করা, opening book যোগ করা, iterative deepening, transposition table ইত্যাদি।

**আনন্দ করে বানাবেন ও পরিবর্তন করবেন — শুভকামনা!**
