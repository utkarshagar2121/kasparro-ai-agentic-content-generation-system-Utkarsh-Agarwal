from product_input import product_raw_data
from agents.parser_agent import ParserAgent
from agents.question_agent import QuestionAgent
from agents.logic_agent import LogicAgent
from agents.template_agent import TemplateAgent
from agents.json_agent import JSONOutputAgent


def run_pipeline():
    parser_agent = ParserAgent()
    question_agent = QuestionAgent()
    logic_agent = LogicAgent()
    template_agent = TemplateAgent()
    json_agent = JSONOutputAgent(output_dir="output")
    product = parser_agent.parse(product_raw_data)
    print(" Parsed product data.")
    questions = question_agent.generate_questions(product)
    print(" Generated categorized questions.")
    logic_blocks = {
        "benefits": logic_agent.generate_benefits_block(product),
        "usage": logic_agent.generate_usage_block(product),
        "side_effects": logic_agent.generate_side_effects_block(product),
        "price": logic_agent.generate_price_block(product),
        "comparison": logic_agent.generate_comparison_block(product)
    }
    print(" Generated content logic blocks.")
    faq_page = template_agent.build_faq_page(product, questions, logic_blocks)
    product_page = template_agent.build_product_page(product, logic_blocks)
    comparison_page = template_agent.build_comparison_page(product, logic_blocks)
    print(" Assembled FAQ, Product, and Comparison pages.")
    json_agent.save_faq_page(faq_page)
    json_agent.save_product_page(product_page)
    json_agent.save_comparison_page(comparison_page)
    print("🎉 All pages saved as JSON in the output/ directory.")


if __name__ == "__main__":
    run_pipeline()
