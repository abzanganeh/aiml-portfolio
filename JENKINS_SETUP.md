git statuscd /Users/admin/Desktop/WebSite

# Create enhanced Chapter 3 with detailed classification explanations
cat > tutorials/ml-fundamentals/chapter3.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 3: Classification Algorithms - Ali Zanganeh</title>
    <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
    <header class="azbn-header">
        <div class="azbn-container">
            <h1><a href="../../" style="text-decoration: none; color: #4f46e5;">Ali Zanganeh</a></h1>
            <nav>
                <a href="../../#home">Home</a>
                <a href="../">Tutorials</a>
                <a href="./chapter2.html">← Chapter 2</a>
                <a href="../../tutorials/neural-networks/">Neural Networks →</a>
            </nav>
        </div>
    </header>

    <main style="padding-top: 100px;">
        <section class="azbn-section">
            <div class="azbn-container">
                <h1>Chapter 3: Classification Algorithms Mastery</h1>
                <p class="azbn-subtitle">From logistic regression to support vector machines with mathematical foundations and real-world applications</p>
                
                <div class="azbn-card" style="background: linear-gradient(135deg, #e91e63 0%, #673ab7 100%); color: white; margin-bottom: 2rem;">
                    <h2>🎯 Learning Objectives</h2>
                    <ul style="color: white;">
                        <li>Master logistic regression theory and sigmoid function mathematics</li>
                        <li>Understand Support Vector Machines and kernel methods</li>
                        <li>Learn comprehensive model evaluation (accuracy, precision, recall, F1, ROC-AUC)</li>
                        <li>Apply hyperparameter tuning with GridSearchCV and cross-validation</li>
                        <li>Handle multi-class classification strategies</li>
                        <li>Recognize and address class imbalance problems</li>
                    </ul>
                </div>

                <h2>🎯 What is Classification?</h2>
                <div class="azbn-card">
                    <h3>From Continuous to Discrete Predictions</h3>
                    <p><strong>Classification</strong> is a supervised learning task where we predict discrete categories or classes rather than continuous values. Unlike regression, the output is categorical.</p>
                    
                    <div style="background: #e8f5e8; padding: 1.5rem; border-radius: 10px; margin: 1.5rem 0;">
                        <h4>🎯 The Classification Problem:</h4>
                        <div style="text-align: center; font-size: 1.2rem; margin: 1rem 0;">
                            <strong>y ∈ {C₁, C₂, ..., Cₖ}</strong>
                        </div>
                        <ul style="margin-top: 1rem;">
                            <li><strong>y:</strong> Target class (what we want to predict)</li>
                            <li><strong>Cₖ:</strong> Possible classes (finite, discrete set)</li>
                            <li><strong>X:</strong> Input features (same as regression)</li>
                            <li><strong>Goal:</strong> Learn P(y|X) - probability of class given features</li>
                        </ul>
                    </div>

                    <h4>📊 Types of Classification Problems:</h4>
                    <div class="azbn-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1rem 0;">
                        <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 8px; background: #e3f2fd;">
                            <h5>🔵 Binary Classification</h5>
                            <p><strong>Classes:</strong> 2 (Yes/No, True/False)</p>
                            <p><strong>Examples:</strong></p>
                            <ul style="font-size: 0.9rem;">
                                <li>Email: Spam vs Ham</li>
                                <li>Medical: Disease vs Healthy</li>
                                <li>Finance: Fraud vs Legitimate</li>
                                <li>Marketing: Buy vs Don't Buy</li>
                            </ul>
                        </div>
                        <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 8px; background: #e8f5e8;">
                            <h5>🟢 Multi-class Classification</h5>
                            <p><strong>Classes:</strong> 3+ (mutually exclusive)</p>
                            <p><strong>Examples:</strong></p>
                            <ul style="font-size: 0.9rem;">
                                <li>Image: Cat, Dog, Bird, Fish</li>
                                <li>Text: Sports, Politics, Entertainment</li>
                                <li>Iris: Setosa, Versicolor, Virginica</li>
                                <li>Grade: A, B, C, D, F</li>
                            </ul>
                        </div>
                        <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 8px; background: #fff8e1;">
                            <h5>🟡 Multi-label Classification</h5>
                            <p><strong>Classes:</strong> Multiple labels per sample</p>
                            <p><strong>Examples:</strong></p>
                            <ul style="font-size: 0.9rem;">
                                <li>Movie genres: Action + Comedy</li>
                                <li>Article tags: Tech + AI + Python</li>
                                <li>Image tags: Person + Car + Road</li>
                                <li>Skills: Python + ML + Statistics</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <h2>📈 Logistic Regression: The Classification Foundation</h2>
                <div class="azbn-card">
                    <h3>From Linear to Probabilistic</h3>
                    
                    <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h4>🤔 Why Not Linear Regression for Classification?</h4>
                        <div style="background: #ffebee; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                            <h5>❌ Problems with Linear Regression:</h5>
                            <ul>
                                <li>Predictions can be <0 or >1 (impossible probabilities)</li>
                                <li>Assumes linear relationship between X and y</li>
                                <li>Equal intervals assumption doesn't make sense for categories</li>
                                <li>Sensitive to outliers in classification context</li>
                            </ul>
                        </div>
                        
                        <div style="background: #e8f5e8; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                            <h5>✅ Logistic Regression Solution:</h5>
                            <ul>
                                <li>Outputs probabilities between 0 and 1</li>
                                <li>Uses sigmoid function to "squash" linear output</li>
                                <li>Models log-odds (logit) as linear function</li>
                                <li>More robust to outliers</li>
                            </ul>
                        </div>
                    </div>

                    <h4>🌊 The Sigmoid Function: Heart of Logistic Regression</h4>
                    <div style="background: #e3f2fd; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <div style="background: white; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                            <h5>📐 Sigmoid Formula:</h5>
                            <div style="text-align: center; font-size: 1.3rem; margin: 1rem 0;">
                                <strong>σ(z) = 1 / (1 + e^(-z))</strong>
                            </div>
                            <p style="text-align: center;">Where z = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ</p>
                        </div>

                        <h5>🎯 Sigmoid Properties:</h5>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                            <div style="background: #f8f9fa; padding: 1rem; border-radius: 6px;">
                                <h6>📊 Mathematical Properties:</h6>
                                <ul style="font-size: 0.9rem;">
                                    <li>Range: (0, 1) - perfect for probabilities</li>
                                    <li>S-shaped curve</li>
                                    <li>Symmetric around z = 0</li>
                                    <li>σ(0) = 0.5 (decision boundary)</li>
                                    <li>σ(∞) = 1, σ(-∞) = 0</li>
                                </ul>
                            </div>
                            <div style="background: #f8f9fa; padding: 1rem; border-radius: 6px;">
                                <h6>🔄 Interpretations:</h6>
                                <ul style="font-size: 0.9rem;">
                                    <li>z > 0 → P(y=1) > 0.5</li>
                                    <li>z < 0 → P(y=1) < 0.5</li>
                                    <li>|z| large → More confident prediction</li>
                                    <li>z ≈ 0 → Uncertain (near boundary)</li>
                                </ul>
                            </div>
                        </div>

                        <div style="background: #fff3e0; padding: 1rem; border-radius: 6px; margin-top: 1rem;">
                            <strong>💡 Key Insight:</strong> The sigmoid transforms any real number into a probability, making it perfect for classification!
                        </div>
                    </div>

                    <h4>🎯 Odds and Log-Odds (Logits)</h4>
                    <div style="background: #f3e5f5; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h5>🎲 Understanding Odds:</h5>
                        <div style="background: white; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                            <p><strong>Probability:</strong> P(y=1) = p</p>
                            <p><strong>Odds:</strong> Odds = p / (1-p)</p>
                            <p><strong>Log-Odds (Logit):</strong> log(Odds) = log(p/(1-p))</p>
                        </div>

                        <h5>🔗 The Beautiful Connection:</h5>
                        <div style="background: white; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                            <div style="text-align: center; margin: 0.5rem 0;">
                                <strong>log(p/(1-p)) = β₀ + β₁x₁ + ... + βₚxₚ</strong>
                            </div>
                            <p style="text-align: center; font-size: 0.9rem;">The log-odds is linear in the parameters!</p>
                        </div>

                        <h5>📊 Interpretation Examples:</h5>
                        <ul>
                            <li><strong>p = 0.5:</strong> Odds = 1:1, Log-Odds = 0</li>
                            <li><strong>p = 0.8:</strong> Odds = 4:1, Log-Odds = 1.39</li>
                            <li><strong>p = 0.1:</strong> Odds = 1:9, Log-Odds = -2.20</li>
                        </ul>

                        <div style="background: #e3f2fd; padding: 1rem; border-radius: 6px; margin-top: 1rem;">
                            <strong>🎯 Coefficient Interpretation:</strong> βⱼ represents the change in log-odds for a one-unit increase in xⱼ
                        </div>
                    </div>

                    <h4>🔢 Maximum Likelihood Estimation</h4>
                    <div style="background: #fff8e1; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h5>🎯 How Logistic Regression Learns:</h5>
                        <p>Unlike linear regression (which uses least squares), logistic regression uses Maximum Likelihood Estimation (MLE).</p>

                        <div style="background: white; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                            <h6>📐 Likelihood Function:</h6>
                            <div style="text-align: center; margin: 0.5rem 0;">
                                <strong>L(β) = ∏ᵢ pᵢ^yᵢ × (1-pᵢ)^(1-yᵢ)</strong>
                            </div>
                            <p style="font-size: 0.9rem; text-align: center;">Where pᵢ = σ(βᵀxᵢ)</p>
                        </div>

                        <h6>🔄 The Process:</h6>
                        <ol>
                            <li><strong>Log-Likelihood:</strong> Take log for easier computation</li>
                            <li><strong>Optimization:</strong> Use gradient descent or Newton-Raphson</li>
                            <li><strong>No Closed Form:</strong> Unlike linear regression, requires iterative methods</li>
                            <li><strong>Convergence:</strong> Algorithm stops when improvement is minimal</li>
                        </ol>

                        <div style="background: #e8f5e8; padding: 1rem; border-radius: 6px; margin-top: 1rem;">
                            <strong>💡 Intuition:</strong> Find parameters that make the observed data most likely under our model!
                        </div>
                    </div>
                </div>

                <h2>⚡ Support Vector Machines: Maximum Margin Classification</h2>
                <div class="azbn-card">
                    <h3>Finding the Optimal Decision Boundary</h3>
                    
                    <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h4>🎯 The SVM Philosophy</h4>
                        <p>SVMs find the decision boundary that maximizes the margin between classes. This leads to better generalization than just finding any boundary that separates the data.</p>

                        <div style="background: #e3f2fd; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                            <h5>🔍 Key Concepts:</h5>
                            <ul>
                                <li><strong>Hyperplane:</strong> Decision boundary (line in 2D, plane in 3D, etc.)</li>
                                <li><strong>Margin:</strong> Distance from boundary to nearest data points</li>
                                <li><strong>Support Vectors:</strong> Data points that define the margin</li>
                                <li><strong>Maximum Margin:</strong> Choose boundary with largest possible margin</li>
                            </ul>
                        </div>

                        <div style="background: white; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                            <h5>📐 Mathematical Formulation:</h5>
                            <p><strong>Hyperplane equation:</strong> wᵀx + b = 0</p>
                            <p><strong>Classification rule:</strong> sign(wᵀx + b)</p>
                            <p><strong>Margin:</strong> 2/||w|| (geometric interpretation)</p>
                            <div style="text-align: center; margin: 0.5rem 0; background: #f8f9fa; padding: 0.5rem; border-radius: 4px;">
                                <strong>Maximize: 2/||w|| ⟺ Minimize: ½||w||²</strong>
                            </div>
                        </div>
                    </div>

                    <h4>🛡️ Hard vs Soft Margin</h4>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
                        <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px;">
                            <h5>🔒 Hard Margin SVM</h5>
                            <p><strong>Assumption:</strong> Data is linearly separable</p>
                            <ul style="font-size: 0.9rem;">
                                <li>No misclassification allowed</li>
                                <li>All points must be on correct side</li>
                                <li>Strict margin enforcement</li>
                                <li>Can fail if data not separable</li>
                            </ul>
                            <div style="background: #f1f8e9; padding: 0.5rem; border-radius: 4px; margin-top: 0.5rem;">
                                <strong>Use when:</strong> Clean, separable data
                            </div>
                        </div>

                        <div style="background: #fff8e1; padding: 1rem; border-radius: 8px;">
                            <h5>🔓 Soft Margin SVM</h5>
                            <p><strong>Reality:</strong> Allow some misclassification</p>
                            <ul style="font-size: 0.9rem;">
                                <li>Introduces slack variables (ξᵢ)</li>
                                <li>Penalty parameter C controls trade-off</li>
                                <li>Balance between margin and errors</li>
                                <li>More robust to outliers</li>
                            </ul>
                            <div style="background: #fef7e0; padding: 0.5rem; border-radius: 4px; margin-top: 0.5rem;">
                                <strong>Use when:</strong> Real-world, noisy data
                            </div>
                        </div>
                    </div>

                    <div style="background: #f3e5f5; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <h4>⚖️ The C Parameter Trade-off:</h4>
                        <ul>
                            <li><strong>Large C:</strong> Low tolerance for errors, may overfit</li>
                            <li><strong>Small C:</strong> High tolerance for errors, may underfit</li>
                            <li><strong>Optimal C:</strong> Found through cross-validation</li>
                        </ul>
                    </div>

                    <h4>🌟 Kernel Methods: The Magic of Non-Linear Classification</h4>
                    <div style="background: #e3f2fd; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h5>🤔 The Non-Linear Problem:</h5>
                        <p>Real-world data is rarely linearly separable. Kernels allow SVMs to create non-linear decision boundaries without explicitly computing high-dimensional transformations.</p>

                        <div style="background: white; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                            <h6>🎯 The Kernel Trick:</h6>
                            <p>Instead of explicitly mapping to higher dimensions, kernels compute similarity in the transformed space:</p>
                            <div style="text-align: center; margin: 0.5rem 0;">
                                <strong>K(xᵢ, xⱼ) = φ(xᵢ)ᵀ φ(xⱼ)</strong>
                            </div>
                            <p style="font-size: 0.9rem; text-align: center;">Compute dot product in feature space without explicit mapping!</p>
                        </div>

                        <h5>🔧 Common Kernel Functions:</h5>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin: 1rem 0;">
                            <div style="background: #f8f9fa; padding: 1rem; border-radius: 6px;">
                                <h6>📏 Linear Kernel</h6>
                                <div style="background: white; padding: 0.5rem; border-radius: 4px; margin: 0.3rem 0;">
                                    <strong>K(x,z) = xᵀz</strong>
                                </div>
                                <p style="font-size: 0.9rem;"><strong>Use:</strong> High-dimensional data, text classification</p>
                            </div>

                            <div style="background: #f8f9fa; padding: 1rem; border-radius: 6px;">
                                <h6>🌀 RBF (Gaussian) Kernel</h6>
                                <div style="background: white; padding: 0.5rem; border-radius: 4px; margin: 0.3rem 0;">
                                    <strong>K(x,z) = exp(-γ||x-z||²)</strong>
                                </div>
                                <p style="font-size: 0.9rem;"><strong>Use:</strong> Most popular, handles complex patterns</p>
                            </div>

                            <div style="background: #f8f9fa; padding: 1rem; border-radius: 6px;">
                                <h6>📐 Polynomial Kernel</h6>
                                <div style="background: white; padding: 0.5rem; border-radius: 4px; margin: 0.3rem 0;">
                                    <strong>K(x,z) = (γxᵀz + r)ᵈ</strong>
                                </div>
                                <p style="font-size: 0.9rem;"><strong>Use:</strong> Natural language processing, image processing</p>
                            </div>

                            <div style="background: #f8f9fa; padding: 1rem; border-radius: 6px;">
                                <h6>〰️ Sigmoid Kernel</h6>
                                <div style="background: white; padding: 0.5rem; border-radius: 4px; margin: 0.3rem 0;">
                                    <strong>K(x,z) = tanh(γxᵀz + r)</strong>
                                </div>
                                <p style="font-size: 0.9rem;"><strong>Use:</strong> Neural network-like behavior</p>
                            </div>
                        </div>

                        <div style="background: #e8f5e8; padding: 1rem; border-radius: 6px; margin-top: 1rem;">
                            <h6>⚙️ Kernel Hyperparameters:</h6>
                            <ul style="margin: 0.5rem 0; font-size: 0.9rem;">
                                <li><strong>γ (gamma):</strong> Controls kernel bandwidth (higher γ = more complex boundary)</li>
                                <li><strong>d (degree):</strong> Polynomial degree (higher d = more complex)</li>
                                <li><strong>r (coef0):</strong> Independent term in polynomial/sigmoid</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <h2>📊 Multi-Class Classification Strategies</h2>
                <div class="azbn-card">
                    <h3>Extending Binary Classifiers</h3>
                    
                    <div style="background: #fff8e1; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h4>🤔 The Multi-Class Challenge</h4>
                        <p>Many algorithms (like SVM) are naturally binary. To handle multiple classes, we need strategies to combine binary classifiers.</p>

                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                            <div style="background: #e3f2fd; padding: 1rem; border-radius: 8px;">
                                <h5>1️⃣ One-vs-Rest (OvR)</h5>
                                <p><strong>Strategy:</strong> Train k binary classifiers (one per class)</p>
                                <ul style="font-size: 0.9rem;">
                                    <li>Class 1 vs {2,3,...,k}</li>
                                    <li>Class 2 vs {1,3,...,k}</li>
                                    <li>...</li>
                                    <li>Choose class with highest confidence</li>
                                </ul>
                                <div style="background: #f8f9fa; padding: 0.5rem; border-radius: 4px; margin-top: 0.5rem;">
                                    <strong>Pros:</strong> Simple, efficient, interpretable
                                </div>
                            </div>

                            <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px;">
                                <h5>2️⃣ One-vs-One (OvO)</h5>
                                <p><strong>Strategy:</strong> Train k(k-1)/2 binary classifiers</p>
                                <ul style="font-size: 0.9rem;">
                                    <li>Class 1 vs Class 2</li>
                                    <li>Class 1 vs Class 3</li>
                                    <li>...</li>
                                    <li>Majority voting for final prediction</li>
                                </ul>
                                <div style="background: #f8f9fa; padding: 0.5rem; border-radius: 4px; margin-top: 0.5rem;">
                                    <strong>Pros:</strong> More robust, smaller training sets per classifier
                                </div>
                            </div>
                        </div>

                        <div style="background: #f3e5f5; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                            <h5>3️⃣ Native Multi-Class</h5>
                            <p>Some algorithms handle multi-class naturally:</p>
                            <ul style="font-size: 0.9rem;">
                                <li><strong>Logistic Regression:</strong> Multinomial/softmax extension</li>
                                <li><strong>Decision Trees:</strong> Split on multiple classes directly</li>
                                <li><strong>Random Forest:</strong> Inherits from decision trees</li>
                                <li><strong>Neural Networks:</strong> Multiple output neurons</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <h2>📏 Classification Evaluation Metrics: Beyond Accuracy</h2>
                <div class="azbn-card">
                    <h3>The Complete Evaluation Toolkit</h3>
                    
                    <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h4>🎯 The Confusion Matrix Foundation</h4>
                        <p>All classification metrics derive from the confusion matrix - a table showing actual vs predicted classifications.</p>

                        <div style="background: white; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; text-align: center;">
                            <h5>📊 Binary Classification Confusion Matrix:</h5>
                            <table style="margin: 1rem auto; border-collapse: collapse; border: 2px solid #333;">
                                <tr style="background: #f0f0f0;">
                                    <td rowspan="2" style="border: 1px solid #333; padding: 0.5rem; font-weight: bold;"></td>
                                    <td colspan="2" style="border: 1px solid #333; padding: 0.5rem; font-weight: bold;">Predicted</td>
                                </tr>
                                <tr style="background: #f0f0f0;">
                                    <td style="border: 1px solid #333; padding: 0.5rem; font-weight: bold;">Negative (0)</td>
                                    <td style="border: 1px solid #333; padding: 0.5rem; font-weight: bold;">Positive (1)</td>
                                </tr>
                                <tr>
                                    <td style="border: 1px solid #333; padding: 0.5rem; font-weight: bold; background: #f0f0f0;">Actual Negative (0)</td>
                                    <td style="border: 1px solid #333; padding: 0.5rem; background: #e8f5e8;"><strong>TN</strong><br>True Negative</td>
                                    <td style="border: 1px solid #333; padding: 0.5rem; background: #ffebee;"><strong>FP</strong><br>False Positive<br>(Type I Error)</td>
                                </tr>
                                <tr>
                                    <td style="border: 1px solid #333; padding: 0.5rem; font-weight: bold; background: #f0f0f0;">Actual Positive (1)</td>
                                    <td style="border: 1px solid #333; padding: 0.5rem; background: #ffebee;"><strong>FN</strong><br>False Negative<br>(Type II Error)</td>
                                    <td style="border: 1px solid #333; padding: 0.5rem; background: #e8f5e8;"><strong>TP</strong><br>True Positive</td>
                                </tr>
                            </table>
                        </div>
                    </div>

                    <h4>📊 Essential Classification Metrics</h4>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
                        <div style="background: #e3f2fd; padding: 1rem; border-radius: 8px;">
                            <h5>🎯 Accuracy</h5>
                            <div style="background: white; padding: 0.5rem; border-radius: 4px; margin: 0.5rem 0; text-align: center;">
                                <strong>(TP + TN) / (TP + TN + FP + FN)</strong>
                            </div>
                            <p><strong>Interpretation:</strong> Overall correctness</p>
                            <p><strong>Good when:</strong> Balanced classes</p>
                            <p><strong>Problem:</strong> Misleading with imbalanced data</p>
                            <div style="background: #f8f9fa; padding: 0.5rem; border-radius: 4px; margin-top: 0.5rem;">
                                <strong>Example:</strong> 95% accuracy sounds great, but not if 95% of data is one class!
                            </div>
                        </div>

                        <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px;">
                            <h5>🔍 Precision</h5>
                            <div style="background: white; padding: 0.5rem; border-radius: 4px; margin: 0.5rem 0; text-align: center;">
                                <strong>TP / (TP + FP)</strong>
                            </div>
                            <p><strong>Interpretation:</strong> Of predicted positives, how many are actually positive?</p>
                            <p><strong>Focus:</strong> Avoiding false alarms</p>
                            <p><strong>Important when:</strong> False positives are costly</p>
                            <div style="background: #f8f9fa; padding: 0.5rem; border-radius: 4px; margin-top: 0.5rem;">
                                <strong>Example:</strong> Medical diagnosis - don't want to scare healthy patients
                            </div>
                        </div>

                        <div style="background: #fff8e1; padding: 1rem; border-radius: 8px;">
                            <h5>🕵️ Recall (Sensitivity)</h5>
                            <div style="background: white; padding: 0.5rem; border-radius: 4px; margin: 0.5rem 0; text-align: center;">
                                <strong>TP / (TP + FN)</strong>
                            </div>
                            <p><strong>Interpretation:</strong> Of actual positives, how many did we catch?</p>
                            <p><strong>Focus:</strong> Avoiding missed cases</p>
                            <p><strong>Important when:</strong> False negatives are costly</p>
                            <div style="background: #f8f9fa; padding: 0.5rem; border-radius: 4px; margin-top: 0.5rem;">
                                <strong>Example:</strong> Cancer screening - don't want to miss any cases
                            </div>
                        </div>

                        <div style="background: #f3e5f5; padding: 1rem; border-radius: 8px;">
                            <h5>⚖️ F1-Score</h5>
                            <div style="background: white; padding: 0.5rem; border-radius: 4px; margin: 0.5rem 0; text-align: center;">
                                <strong>2 × (Precision × Recall) / (Precision + Recall)</strong>
                            </div>
                            <p><strong>Interpretation:</strong> Harmonic mean of precision and recall</p>
                            <p><strong>Good when:</strong> Need balance between precision and recall</p>
                            <p><strong>Range:</strong> 0 to 1 (higher is better)</p>
                            <div style="background: #f8f9fa; padding: 0.5rem; border-radius: 4px; margin-top: 0.5rem;">
                                <strong>Use case:</strong> Imbalanced data, general performance metric
                            </div>
                        </div>
                    </div>

                    <h4>📈 ROC Curve and AUC: Threshold-Independent Evaluation</h4>
                    <div style="background: #e3f2fd; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h5>🎯 ROC (Receiver Operating Characteristic) Curve</h5>
                        <p>Plots True Positive Rate vs False Positive Rate at various classification thresholds.</p>

                        <div style="background: white; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                                <div>
                                    <p><strong>True Positive Rate (TPR):</strong></p>
                                    <div style="text-align: center; background: #f8f9fa; padding: 0.5rem; border-radius: 4px;">
                                        TPR = TP / (TP + FN) = Recall
                                    </div>
                                </div>
                                <div>
                                    <p><strong>False Positive Rate (FPR):</strong></p>
                                    <div style="text-align: center; background: #f8f9fa; padding: 0.5rem; border-radius: 4px;">
                                        FPR = FP / (FP + TN)
                                    </div>
                                </div>
                            </div>
                        </div>

                        <h5>📊 AUC (Area Under Curve) Interpretation:</h5>
                        <ul>
                            <li><strong>AUC = 1.0:</strong> Perfect classifier</li>
                            <li><strong>AUC = 0.9-1.0:</strong> Excellent</li>
                            <li><strong>AUC = 0.8-0.9:</strong> Good</li>
                            <li><strong>AUC = 0.7-0.8:</strong> Fair</li>
                            <li><strong>AUC = 0.6-0.7:</strong> Poor</li>
                            <li><strong>AUC = 0.5:</strong> Random guessing</li>
                            <li><strong>AUC < 0.5:</strong> Worse than random (invert predictions!)</li>
                        </ul>

                        <div style="background: #e8f5e8; padding: 1rem; border-radius: 6px; margin-top: 1rem;">
                            <strong>💡 AUC Advantage:</strong> Single number summarizing performance across all thresholds - great for model comparison!
                        </div>
                    </div>
                </div>

                <h2>🔧 Hyperparameter Tuning: Optimizing Model Performance</h2>
                <div class="azbn-card">
                    <h3>GridSearchCV and Cross-Validation Mastery</h3>
                    
                    <div style="background: #fff8e1; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h4>🎯 The Hyperparameter Challenge</h4>
                        <p>Unlike model parameters (learned from data), hyperparameters are set before training and control the learning process. Finding optimal values requires systematic search.</p>

                        <h5>🔍 Key Hyperparameters by Algorithm:</h5>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin: 1rem 0;">
                            <div style="background: #e3f2fd; padding: 1rem; border-radius: 6px;">
                                <h6>📈 Logistic Regression</h6>
                                <ul style="font-size: 0.9rem;">
                                    <li><strong>C:</strong> Regularization strength</li>
                                    <li><strong>penalty:</strong> 'l1', 'l2', 'elasticnet'</li>
                                    <li><strong>solver:</strong> Optimization algorithm</li>
                                    <li><strong>max_iter:</strong> Maximum iterations</li>
                                </ul>
                            </div>
                            <div style="background: #e8f5e8; padding: 1rem; border-radius: 6px;">
                                <h6>⚡ SVM</h6>
                                <ul style="font-size: 0.9rem;">
                                    <li><strong>C:</strong> Penalty parameter</li>
                                    <li><strong>kernel:</strong> 'linear', 'rbf', 'poly'</li>
                                    <li><strong>gamma:</strong> Kernel coefficient</li>
                                    <li><strong>degree:</strong> Polynomial degree</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <h4>🔍 Search Strategies</h4>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
                        <div style="background: #e3f2fd; padding: 1rem; border-radius: 8px;">
                            <h5>🌐 Grid Search</h5>
                            <p><strong>Strategy:</strong> Exhaustive search over parameter grid</p>
                            <ul style="font-size: 0.9rem;">
                                <li>Define parameter ranges/values</li>
                                <li>Try every combination</li>
                                <li>Computationally expensive but thorough</li>
                                <li>Guaranteed to find best in grid</li>
                            </ul>
                            <div style="background: #f8f9fa; padding: 0.5rem; border-radius: 4px; margin-top: 0.5rem;">
                                <strong>Best for:</strong> Small parameter spaces, final tuning
                            </div>
                        </div>

                        <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px;">
                            <h5>🎲 Random Search</h5>
                            <p><strong>Strategy:</strong> Randomly sample parameter combinations</p>
                            <ul style="font-size: 0.9rem;">
                                <li>Define parameter distributions</li>
                                <li>Sample N random combinations</li>
                                <li>More efficient for high dimensions</li>
                                <li>Often finds good solutions faster</li>
                            </ul>
                            <div style="background: #f8f9fa; padding: 0.5rem; border-radius: 4px; margin-top: 0.5rem;">
                                <strong>Best for:</strong> Large parameter spaces, initial exploration
                            </div>
                        </div>
                    </div>

                    <h4>📊 Cross-Validation: Robust Performance Estimation</h4>
                    <div style="background: #f3e5f5; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h5>🔄 K-Fold Cross-Validation Process:</h5>
                        <ol>
                            <li><strong>Split data into K folds</strong> (usually K=5 or K=10)</li>
                            <li><strong>For each fold:</strong>
                                <ul style="margin-left: 1rem;">
                                    <li>Train on K-1 folds</li>
                                    <li>Validate on remaining fold</li>
                                    <li>Record performance metric</li>
                                </ul>
                            </li>
                            <li><strong>Average performance</strong> across all folds</li>
                            <li><strong>Standard deviation</strong> indicates stability</li>
                        </ol>

                        <div style="background: white; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                            <h6>🎯 Benefits of Cross-Validation:</h6>
                            <ul style="font-size: 0.9rem;">
                                <li>More robust than single train-test split</li>
                                <li>Uses all data for both training and validation</li>
                                <li>Provides estimate of model variance</li>
                                <li>Reduces dependence on specific data split</li>
                            </ul>
                        </div>

                        <div style="background: #e8f5e8; padding: 1rem; border-radius: 6px; margin-top: 1rem;">
                            <h6>⚠️ Important Considerations:</h6>
                            <ul style="font-size: 0.9rem;">
                                <li><strong>Stratification:</strong> Preserve class distribution in each fold</li>
                                <li><strong>Time series:</strong> Use TimeSeriesSplit for temporal data</li>
                                <li><strong>Computational cost:</strong> K times more expensive than single split</li>
                                <li><strong>Nested CV:</strong> For unbiased hyperparameter selection</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <h2>⚖️ Handling Class Imbalance</h2>
                <div class="azbn-card">
                    <h3>When Classes Aren't Equal</h3>
                    
                    <div style="background: #ffebee; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h4>❌ The Imbalanced Data Problem</h4>
                        <p>Many real-world problems have imbalanced classes (e.g., fraud detection: 99.9% legitimate, 0.1% fraud). Standard metrics and algorithms can be misleading.</p>

                        <h5>🚨 Common Issues:</h5>
                        <ul>
                            <li>High accuracy but poor minority class detection</li>
                            <li>Models biased toward majority class</li>
                            <li>Misleading performance metrics</li>
                            <li>Poor generalization to new data</li>
                        </ul>
                    </div>

                    <h4>🛠️ Solutions for Imbalanced Data</h4>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
                        <div style="background: #e3f2fd; padding: 1rem; border-radius: 8px;">
                            <h5>📊 Sampling Techniques</h5>
                            <ul style="font-size: 0.9rem;">
                                <li><strong>Random Oversampling:</strong> Duplicate minority samples</li>
                                <li><strong>Random Undersampling:</strong> Remove majority samples</li>
                                <li><strong>SMOTE:</strong> Generate synthetic minority samples</li>
                                <li><strong>Tomek Links:</strong> Remove borderline samples</li>
                            </ul>
                        </div>

                        <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px;">
                            <h5>⚖️ Algorithm Modifications</h5>
                            <ul style="font-size: 0.9rem;">
                                <li><strong>Class Weights:</strong> Penalize misclassification differently</li>
                                <li><strong>Threshold Tuning:</strong> Adjust decision boundary</li>
                                <li><strong>Cost-Sensitive Learning:</strong> Incorporate misclassification costs</li>
                                <li><strong>Ensemble Methods:</strong> Combine multiple models</li>
                            </ul>
                        </div>

                        <div style="background: #fff8e1; padding: 1rem; border-radius: 8px;">
                            <h5>📏 Evaluation Adjustments</h5>
                            <ul style="font-size: 0.9rem;">
                                <li><strong>Focus on F1-Score:</strong> Instead of accuracy</li>
                                <li><strong>Precision-Recall Curves:</strong> Better than ROC for imbalanced data</li>
                                <li><strong>Balanced Accuracy:</strong> Average of per-class accuracies</li>
                                <li><strong>Matthews Correlation:</strong> Considers all confusion matrix elements</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <h2>🎯 Key Takeaways and Best Practices</h2>
                <div class="azbn-deployment-status">
                    <p><strong>✅ Chapter 3 Mastery:</strong></p>
                    <p>• Logistic regression with sigmoid function and maximum likelihood</p>
                    <p>• SVM with kernel methods and margin maximization theory</p>
                    <p>• Comprehensive evaluation metrics beyond accuracy</p>
                    <p>• Multi-class classification strategies and implementations</p>
                    <p>• Hyperparameter tuning with cross-validation best practices</p>
                    <p>• Class imbalance handling and robust evaluation techniques</p>
                </div>

                <div style="background: #e3f2fd; padding: 1.5rem; border-radius: 10px; margin: 2rem 0;">
                    <h3>🎓 Professional Classification Guidelines:</h3>
                    <ol>
                        <li><strong>Start with simple baselines:</strong> Logistic regression before complex models</li>
                        <li><strong>Understand your data:</strong> Check class distribution and feature relationships</li>
                        <li><strong>Choose appropriate metrics:</strong> F1-score for imbalanced, AUC for ranking</li>
                        <li><strong>Use proper validation:</strong> Stratified K-fold cross-validation</li>
                        <li><strong>Tune hyperparameters systematically:</strong> Grid/random search with CV</li>
                        <li><strong>Address class imbalance:</strong> Use appropriate techniques and metrics</li>
                        <li><strong>Interpret results carefully:</strong> Understand what your model is learning</li>
                        <li><strong>Consider business context:</strong> Precision vs recall trade-offs matter</li>
                    </ol>
                </div>

                <div style="margin: 2rem 0; text-align: center;">
                    <a href="./chapter2.html" class="azbn-btn azbn-secondary" style="text-decoration: none; margin-right: 1rem;">← Chapter 2: Regression</a>
                    <a href="../../tutorials/neural-networks/" class="azbn-btn" style="text-decoration: none;">Next: Neural Networks →</a>
                    <a href="./index.html" class="azbn-btn azbn-secondary" style="text-decoration: none; margin-left: 1rem;">Course Home</a>
                </div>
            </div>
        </section>
    </main>
</body>
</html>
EOF

# Deploy Chapter 3 enhancement
git add tutorials/ml-fundamentals/chapter3.html
git commit -m "🎯 ENHANCE: Chapter 3 with comprehensive classification mastery

✅ MAJOR IMPROVEMENTS:
- Logistic regression mathematical foundations (sigmoid, odds, MLE)
- SVM theory with kernel methods and margin maximization
- Complete evaluation metrics (precision, recall, F1, ROC-AUC)
- Multi-class classification strategies (OvR, OvO, native)
- Hyperparameter tuning with GridSearchCV best practices
- Class imbalance handling and robust evaluation
- Professional guidelines and business considerations

🎯 EDUCATIONAL EXCELLENCE:
- Mathematical rigor with practical intuition
- Real-world examples and applications
- Professional tips and industry best practices
- Comprehensive coverage from theory to implementation"

git push origin main

echo "🎉 COMPLETE! All 3 chapters now enhanced with comprehensive content!"
echo "🌐 Your ML Fundamentals course is now world-class at:"
echo "https://zanganehai.com/tutorials/ml-fundamentals/"cd /Users/admin/Desktop/WebSite

# Restore the proper JENKINS_SETUP.md
cat > JENKINS_SETUP.md << 'EOF'
# Jenkins Setup Documentation

## Overview
This document outlines the Jenkins CI/CD pipeline setup for the Ali Zanganeh AIML Portfolio.

## Pipeline Configuration
- **Pipeline Name**: website-portfolio-deployment
- **Trigger**: GitHub webhook on push to main branch
- **Agent**: macOS agent (macos-agent)
- **Deployment Target**: srv637-files.hstgr.io

## Deployment Process
1. Code checkout from GitHub repository
2. File validation and preprocessing
3. FTP deployment via lftp to hosting server
4. Deployment verification and status reporting

## Server Details
- **FTP Server**: srv637-files.hstgr.io
- **Target Directory**: /domains/zanganehai.com/public_html/
- **Protocol**: FTP with lftp client

## Status
✅ Jenkins pipeline operational and working
✅ Dual deployment with GitHub Actions
✅ Auto-deployment on code changes

## Recent Deployments
- Enhanced Chapter 1: ML Introduction with comprehensive Python examples
- Enhanced Chapter 2: Regression Analysis with complete implementations
- Enhanced Chapter 3: Classification Algorithms with hands-on coding

## Course Structure
Complete ML Fundamentals course with world-class content and executable Python code examples.
EOF

# Now add comprehensive Python code examples to Chapter 3
cat >> tutorials/ml-fundamentals/chapter3.html << 'EOF'

                <h2>💻 Hands-On Python Implementation</h2>
                <div class="azbn-card">
                    <h3>Classification Projects: From Theory to Practice</h3>
                    
                    <div style="background: #e8f5e8; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h4>📊 Binary Classification: Breast Cancer Detection</h4>
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Import essential libraries</div>
<div><span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">numpy</span> <span style="color: #f92672;">as</span> <span style="color: #f8f8f2;">np</span></div>
<div><span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">pandas</span> <span style="color: #f92672;">as</span> <span style="color: #f8f8f2;">pd</span></div>
<div><span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">matplotlib.pyplot</span> <span style="color: #f92672;">as</span> <span style="color: #f8f8f2;">plt</span></div>
<div><span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">seaborn</span> <span style="color: #f92672;">as</span> <span style="color: #f8f8f2;">sns</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.datasets</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">load_breast_cancer</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.model_selection</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">train_test_split, GridSearchCV, cross_val_score</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.preprocessing</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">StandardScaler</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.linear_model</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">LogisticRegression</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.svm</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">SVC</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.metrics</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">accuracy_score, classification_report, confusion_matrix</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.metrics</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">roc_curve, auc, precision_recall_curve</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Load the breast cancer dataset</div>
<div><span style="color: #f8f8f2;">cancer</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">load_breast_cancer()</span></div>
<div><span style="color: #f8f8f2;">df</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">pd.DataFrame(cancer.data, columns=cancer.feature_names)</span></div>
<div><span style="color: #f8f8f2;">df</span><span style="color: #f92672;">[</span><span style="color: #e6db74;">'target'</span><span style="color: #f92672;">]</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">cancer.target</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"Breast Cancer Dataset:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Shape: </span><span style="color: #e6db74;">{df.shape}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Features: </span><span style="color: #e6db74;">{len(cancer.feature_names)}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Classes: </span><span style="color: #e6db74;">{cancer.target_names}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Check class distribution</div>
<div><span style="color: #f8f8f2;">class_counts</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">df</span><span style="color: #f92672;">[</span><span style="color: #e6db74;">'target'</span><span style="color: #f92672;">]</span><span style="color: #f8f8f2;">.value_counts()</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"\nClass Distribution:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Malignant (0): </span><span style="color: #e6db74;">{class_counts[0]}</span><span style="color: #e6db74;"> ({class_counts[0]/len(df)*100:.1f}%)"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Benign (1): </span><span style="color: #e6db74;">{class_counts[1]}</span><span style="color: #e6db74;"> ({class_counts[1]/len(df)*100:.1f}%)"</span><span style="color: #f92672;">)</span></div>
                        </div>

                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Data exploration and visualization</div>
<div><span style="color: #f8f8f2;">plt.figure(figsize=(15, 5))</span></div>

<div style="color: #75715e;"># Class distribution</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 1)</span></div>
<div><span style="color: #f8f8f2;">class_counts.plot(kind=</span><span style="color: #e6db74;">'bar'</span><span style="color: #f8f8f2;">, color=[</span><span style="color: #e6db74;">'lightcoral'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'lightblue'</span><span style="color: #f8f8f2;">])</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Class Distribution'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'Class'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.ylabel(</span><span style="color: #e6db74;">'Count'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.xticks([0, 1], [</span><span style="color: #e6db74;">'Malignant'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'Benign'</span><span style="color: #f8f8f2;">], rotation=0)</span></div>

<div style="color: #75715e;"># Feature correlation heatmap (top 10 features)</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 2)</span></div>
<div><span style="color: #f8f8f2;">top_features</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">df.corr()[</span><span style="color: #e6db74;">'target'</span><span style="color: #f8f8f2;">].abs().nlargest(11).index[1:11]</span></div>
<div><span style="color: #f8f8f2;">corr_matrix</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">df[top_features].corr()</span></div>
<div><span style="color: #f8f8f2;">sns.heatmap(corr_matrix, annot=</span><span style="color: #ae81ff;">False</span><span style="color: #f8f8f2;">, cmap=</span><span style="color: #e6db74;">'coolwarm'</span><span style="color: #f8f8f2;">, center=0)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Top 10 Features Correlation'</span><span style="color: #f8f8f2;">)</span></div>

<div style="color: #75715e;"># Feature importance by correlation with target</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 3)</span></div>
<div><span style="color: #f8f8f2;">feature_corr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">df.corr()[</span><span style="color: #e6db74;">'target'</span><span style="color: #f8f8f2;">].abs().sort_values(ascending=</span><span style="color: #ae81ff;">False</span><span style="color: #f8f8f2;">)[1:11]</span></div>
<div><span style="color: #f8f8f2;">feature_corr.plot(kind=</span><span style="color: #e6db74;">'barh'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Top 10 Features by Target Correlation'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'Absolute Correlation'</span><span style="color: #f8f8f2;">)</span></div>

<div><span style="color: #f8f8f2;">plt.tight_layout()</span></div>
<div><span style="color: #f8f8f2;">plt.show()</span></div>
                        </div>
                    </div>

                    <h4>📈 Logistic Regression Implementation</h4>
                    <div style="background: #e3f2fd; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Prepare data for modeling</div>
<div><span style="color: #f8f8f2;">X</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">cancer.data</span></div>
<div><span style="color: #f8f8f2;">y</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">cancer.target</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Train-test split</div>
<div><span style="color: #f8f8f2;">X_train, X_test, y_train, y_test</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">train_test_split(</span></div>
<div><span style="color: #f8f8f2;">    X, y, test_size=0.2, random_state=42, stratify=y</span></div>
<div><span style="color: #f8f8f2;">)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Training set: </span><span style="color: #e6db74;">{X_train.shape[0]}</span><span style="color: #e6db74;"> samples"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Test set: </span><span style="color: #e6db74;">{X_test.shape[0]}</span><span style="color: #e6db74;"> samples"</span><span style="color: #f92672;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Feature scaling (important for logistic regression)</div>
<div><span style="color: #f8f8f2;">scaler</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">StandardScaler()</span></div>
<div><span style="color: #f8f8f2;">X_train_scaled</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">scaler.fit_transform(X_train)</span></div>
<div><span style="color: #f8f8f2;">X_test_scaled</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">scaler.transform(X_test)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Train logistic regression</div>
<div><span style="color: #f8f8f2;">lr_model</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">LogisticRegression(random_state=42, max_iter=1000)</span></div>
<div><span style="color: #f8f8f2;">lr_model.fit(X_train_scaled, y_train)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Make predictions</div>
<div><span style="color: #f8f8f2;">y_pred_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">lr_model.predict(X_test_scaled)</span></div>
<div><span style="color: #f8f8f2;">y_pred_proba_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">lr_model.predict_proba(X_test_scaled)[:, 1]</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Evaluate performance</div>
<div><span style="color: #f8f8f2;">accuracy_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">accuracy_score(y_test, y_pred_lr)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"\nLogistic Regression Results:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Accuracy: </span><span style="color: #e6db74;">{accuracy_lr:.3f}</span><span style="color: #e6db74;"> (</span><span style="color: #e6db74;">{accuracy_lr*100:.1f}</span><span style="color: #e6db74;">%)"</span><span style="color: #f92672;">)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"\nDetailed Classification Report:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #f8f8f2;">classification_report(y_test, y_pred_lr, target_names=cancer.target_names)</span><span style="color: #f92672;">)</span></div>
                        </div>

                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Analyze coefficients (feature importance)</div>
<div><span style="color: #f8f8f2;">feature_importance_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">pd.DataFrame({</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'feature'</span><span style="color: #f8f8f2;">: cancer.feature_names,</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'coefficient'</span><span style="color: #f8f8f2;">: lr_model.coef_[0],</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'abs_coefficient'</span><span style="color: #f8f8f2;">: np.abs(lr_model.coef_[0])</span></div>
<div><span style="color: #f8f8f2;">}).sort_values(</span><span style="color: #e6db74;">'abs_coefficient'</span><span style="color: #f8f8f2;">, ascending=</span><span style="color: #ae81ff;">False</span><span style="color: #f8f8f2;">)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"\nTop 10 Most Important Features:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #f8f8f2;">feature_importance_lr.head(10)</span><span style="color: #f92672;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Visualization of top features</div>
<div><span style="color: #f8f8f2;">plt.figure(figsize=(10, 6))</span></div>
<div><span style="color: #f8f8f2;">top_10_features</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">feature_importance_lr.head(10)</span></div>
<div><span style="color: #f8f8f2;">plt.barh(</span><span style="color: #66d9ef;">range</span><span style="color: #f92672;">(</span><span style="color: #ae81ff;">10</span><span style="color: #f92672;">)</span><span style="color: #f8f8f2;">, top_10_features[</span><span style="color: #e6db74;">'coefficient'</span><span style="color: #f8f8f2;">])</span></div>
<div><span style="color: #f8f8f2;">plt.yticks(</span><span style="color: #66d9ef;">range</span><span style="color: #f92672;">(</span><span style="color: #ae81ff;">10</span><span style="color: #f92672;">)</span><span style="color: #f8f8f2;">, top_10_features[</span><span style="color: #e6db74;">'feature'</span><span style="color: #f8f8f2;">])</span></div>
<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'Coefficient Value'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Top 10 Feature Coefficients in Logistic Regression'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.axvline(x=0, color=</span><span style="color: #e6db74;">'red'</span><span style="color: #f8f8f2;">, linestyle=</span><span style="color: #e6db74;">'--'</span><span style="color: #f8f8f2;">, alpha=0.7)</span></div>
<div><span style="color: #f8f8f2;">plt.tight_layout()</span></div>
<div><span style="color: #f8f8f2;">plt.show()</span></div>
                        </div>
                    </div>

                    <h4>⚡ Support Vector Machine Implementation</h4>
                    <div style="background: #fff8e1; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># SVM with different kernels</div>
<div><span style="color: #f8f8f2;">kernels</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">[</span><span style="color: #e6db74;">'linear'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'rbf'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'poly'</span><span style="color: #f8f8f2;">]</span></div>
<div><span style="color: #f8f8f2;">svm_results</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">{}</span></div>

<div><span style="color: #f92672;">for</span> <span style="color: #f8f8f2;">kernel</span> <span style="color: #f92672;">in</span> <span style="color: #f8f8f2;">kernels:</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #75715e;"># Train SVM with different kernel</span></div>
<div><span style="color: #f8f8f2;">    svm_model</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">SVC(kernel=kernel, random_state=42, probability=</span><span style="color: #ae81ff;">True</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">    svm_model.fit(X_train_scaled, y_train)</span></div>
    
<div><span style="color: #f8f8f2;">    </span><span style="color: #75715e;"># Predictions</span></div>
<div><span style="color: #f8f8f2;">    y_pred_svm</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">svm_model.predict(X_test_scaled)</span></div>
<div><span style="color: #f8f8f2;">    y_pred_proba_svm</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">svm_model.predict_proba(X_test_scaled)[:, 1]</span></div>
    
<div><span style="color: #f8f8f2;">    </span><span style="color: #75715e;"># Store results</span></div>
<div><span style="color: #f8f8f2;">    accuracy_svm</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">accuracy_score(y_test, y_pred_svm)</span></div>
<div><span style="color: #f8f8f2;">    svm_results[kernel]</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">{</span></div>
<div><span style="color: #f8f8f2;">        </span><span style="color: #e6db74;">'model'</span><span style="color: #f8f8f2;">: svm_model,</span></div>
<div><span style="color: #f8f8f2;">        </span><span style="color: #e6db74;">'accuracy'</span><span style="color: #f8f8f2;">: accuracy_svm,</span></div>
<div><span style="color: #f8f8f2;">        </span><span style="color: #e6db74;">'predictions'</span><span style="color: #f8f8f2;">: y_pred_svm,</span></div>
<div><span style="color: #f8f8f2;">        </span><span style="color: #e6db74;">'probabilities'</span><span style="color: #f8f8f2;">: y_pred_proba_svm</span></div>
<div><span style="color: #f8f8f2;">    }</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Display SVM results</div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"SVM Results with Different Kernels:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"Kernel   | Accuracy"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"-" * 18</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #f92672;">for</span> <span style="color: #f8f8f2;">kernel, results</span> <span style="color: #f92672;">in</span> <span style="color: #f8f8f2;">svm_results.items():</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"</span><span style="color: #e6db74;">{kernel:8s}</span><span style="color: #e6db74;"> | </span><span style="color: #e6db74;">{results['accuracy']:.3f}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Best SVM model</div>
<div><span style="color: #f8f8f2;">best_kernel</span> <span style="color: #f92672;">=</span> <span style="color: #66d9ef;">max</span><span style="color: #f92672;">(</span><span style="color: #f8f8f2;">svm_results, key=</span><span style="color: #f92672;">lambda</span> <span style="color: #f8f8f2;">k: svm_results[k][</span><span style="color: #e6db74;">'accuracy'</span><span style="color: #f8f8f2;">])</span></div>
<div><span style="color: #f8f8f2;">best_svm</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">svm_results[best_kernel]</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"\nBest SVM kernel: </span><span style="color: #e6db74;">{best_kernel}</span><span style="color: #e6db74;"> (Accuracy: </span><span style="color: #e6db74;">{best_svm['accuracy']:.3f}</span><span style="color: #e6db74;">)"</span><span style="color: #f92672;">)</span></div>
                        </div>
                    </div>

                    <h4>🔍 Hyperparameter Tuning with GridSearchCV</h4>
                    <div style="background: #f3e5f5; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># GridSearch for SVM hyperparameters</div>
<div><span style="color: #f8f8f2;">param_grid</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">{</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'C'</span><span style="color: #f8f8f2;">: [0.1, 1, 10, 100],</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'gamma'</span><span style="color: #f8f8f2;">: [</span><span style="color: #e6db74;">'scale'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'auto'</span><span style="color: #f8f8f2;">, 0.001, 0.01, 0.1, 1],</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'kernel'</span><span style="color: #f8f8f2;">: [</span><span style="color: #e6db74;">'rbf'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'poly'</span><span style="color: #f8f8f2;">]</span></div>
<div><span style="color: #f8f8f2;">}</span></div>

<div><span style="color: #f8f8f2;">svm_grid</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">GridSearchCV(</span></div>
<div><span style="color: #f8f8f2;">    SVC(random_state=42, probability=</span><span style="color: #ae81ff;">True</span><span style="color: #f8f8f2;">),</span></div>
<div><span style="color: #f8f8f2;">    param_grid,</span></div>
<div><span style="color: #f8f8f2;">    cv=5,</span></div>
<div><span style="color: #f8f8f2;">    scoring=</span><span style="color: #e6db74;">'accuracy'</span><span style="color: #f8f8f2;">,</span></div>
<div><span style="color: #f8f8f2;">    n_jobs=-1,</span></div>
<div><span style="color: #f8f8f2;">    verbose=1</span></div>
<div><span style="color: #f8f8f2;">)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"Starting GridSearch for SVM hyperparameters..."</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #f8f8f2;">svm_grid.fit(X_train_scaled, y_train)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"\nBest parameters: </span><span style="color: #e6db74;">{svm_grid.best_params_}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Best cross-validation score: </span><span style="color: #e6db74;">{svm_grid.best_score_:.3f}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Evaluate optimized model</div>
<div><span style="color: #f8f8f2;">best_svm_optimized</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">svm_grid.best_estimator_</span></div>
<div><span style="color: #f8f8f2;">y_pred_optimized</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">best_svm_optimized.predict(X_test_scaled)</span></div>
<div><span style="color: #f8f8f2;">accuracy_optimized</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">accuracy_score(y_test, y_pred_optimized)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"\nOptimized SVM Test Accuracy: </span><span style="color: #e6db74;">{accuracy_optimized:.3f}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>
                        </div>
                    </div>

                    <h4>📊 Comprehensive Model Evaluation</h4>
                    <div style="background: #e8f5e8; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Confusion Matrix</div>
<div><span style="color: #f8f8f2;">plt.figure(figsize=(15, 5))</span></div>

<div style="color: #75715e;"># Logistic Regression Confusion Matrix</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 1)</span></div>
<div><span style="color: #f8f8f2;">cm_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">confusion_matrix(y_test, y_pred_lr)</span></div>
<div><span style="color: #f8f8f2;">sns.heatmap(cm_lr, annot=</span><span style="color: #ae81ff;">True</span><span style="color: #f8f8f2;">, fmt=</span><span style="color: #e6db74;">'d'</span><span style="color: #f8f8f2;">, cmap=</span><span style="color: #e6db74;">'Blues'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Logistic Regression\nConfusion Matrix'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'Predicted'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.ylabel(</span><span style="color: #e6db74;">'Actual'</span><span style="color: #f8f8f2;">)</span></div>

<div style="color: #75715e;"># ROC Curves</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 2)</span></div>

<div style="color: #75715e;"># Logistic Regression ROC</div>
<div><span style="color: #f8f8f2;">fpr_lr, tpr_lr, _</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">roc_curve(y_test, y_pred_proba_lr)</span></div>
<div><span style="color: #f8f8f2;">auc_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">auc(fpr_lr, tpr_lr)</span></div>
<div><span style="color: #f8f8f2;">plt.plot(fpr_lr, tpr_lr, label=</span><span style="color: #e6db74;">f'Logistic Regression (AUC = </span><span style="color: #e6db74;">{auc_lr:.3f}</span><span style="color: #e6db74;">)'</span><span style="color: #f8f8f2;">)</span></div>

<div style="color: #75715e;"># SVM ROC</div>
<div><span style="color: #f8f8f2;">y_pred_proba_svm_opt</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">best_svm_optimized.predict_proba(X_test_scaled)[:, 1]</span></div>
<div><span style="color: #f8f8f2;">fpr_svm, tpr_svm, _</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">roc_curve(y_test, y_pred_proba_svm_opt)</span></div>
<div><span style="color: #f8f8f2;">auc_svm</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">auc(fpr_svm, tpr_svm)</span></div>
<div><span style="color: #f8f8f2;">plt.plot(fpr_svm, tpr_svm, label=</span><span style="color: #e6db74;">f'SVM (AUC = </span><span style="color: #e6db74;">{auc_svm:.3f}</span><span style="color: #e6db74;">)'</span><span style="color: #f8f8f2;">)</span></div>

<div><span style="color: #f8f8f2;">plt.plot([0, 1], [0, 1], </span><span style="color: #e6db74;">'k--'</span><span style="color: #f8f8f2;">, label=</span><span style="color: #e6db74;">'Random Classifier'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'False Positive Rate'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.ylabel(</span><span style="color: #e6db74;">'True Positive Rate'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'ROC Curve Comparison'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.legend()</span></div>

<div style="color: #75715e;"># Precision-Recall Curves</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 3)</span></div>

<div><span style="color: #75715e;"># Logistic Regression PR Curve</div>
<div><span style="color: #f8f8f2;">precision_lr, recall_lr, _</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">precision_recall_curve(y_test, y_pred_proba_lr)</span></div>
<div><span style="color: #f8f8f2;">plt.plot(recall_lr, precision_lr, label=</span><span style="color: #e6db74;">'Logistic Regression'</span><span style="color: #f8f8f2;">)</span></div>

<div style="color: #75715e;"># SVM PR Curve</div>
<div><span style="color: #f8f8f2;">precision_svm, recall_svm, _</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">precision_recall_curve(y_test, y_pred_proba_svm_opt)</span></div>
<div><span style="color: #f8f8f2;">plt.plot(recall_svm, precision_svm, label=</span><span style="color: #e6db74;">'SVM'</span><span style="color: #f8f8f2;">)</span></div>

<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'Recall'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.ylabel(</span><span style="color: #e6db74;">'Precision'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Precision-Recall Curve'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.legend()</span></div>

<div><span style="color: #f8f8f2;">plt.tight_layout()</span></div>
<div><span style="color: #f8f8f2;">plt.show()</span></div>
                        </div>
                    </div>

                    <h4>🌍 Multi-Class Classification Example</h4>
                    <div style="background: #e3f2fd; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Multi-class classification with Iris dataset</div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.datasets</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">load_iris</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.multiclass</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">OneVsRestClassifier, OneVsOneClassifier</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Load Iris dataset</div>
<div><span style="color: #f8f8f2;">iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">load_iris()</span></div>
<div><span style="color: #f8f8f2;">X_iris, y_iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">iris.data, iris.target</span></div>

<div><span style="color: #f8f8f2;">X_train_iris, X_test_iris, y_train_iris, y_test_iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">train_test_split(</span></div>
<div><span style="color: #f8f8f2;">    X_iris, y_iris, test_size=0.3, random_state=42, stratify=y_iris</span></div>
<div><span style="color: #f8f8f2;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Scale features</div>
<div><span style="color: #f8f8f2;">scaler_iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">StandardScaler()</span></div>
<div><span style="color: #f8f8f2;">X_train_iris_scaled</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">scaler_iris.fit_transform(X_train_iris)</span></div>
<div><span style="color: #f8f8f2;">X_test_iris_scaled</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">scaler_iris.transform(X_test_iris)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Compare different multi-class strategies</div>
<div><span style="color: #f8f8f2;">strategies</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">{</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'Native'</span><span style="color: #f8f8f2;">: LogisticRegression(random_state=42, max_iter=1000),</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'One-vs-Rest'</span><span style="color: #f8f8f2;">: OneVsRestClassifier(SVC(kernel=</span><span style="color: #e6db74;">'rbf'</span><span style="color: #f8f8f2;">, random_state=42)),</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'One-vs-One'</span><span style="color: #f8f8f2;">: OneVsOneClassifier(SVC(kernel=</span><span style="color: #e6db74;">'rbf'</span><span style="color: #f8f8f2;">, random_state=42))</span></div>
<div><span style="color: #f8f8f2;">}</span></div>

<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"Multi-class Classification Results:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"Strategy      | Accuracy"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"-" * 22</span><span style="color: #f92672;">)</span></div>

<div><span style="color: #f92672;">for</span> <span style="color: #f8f8f2;">name, model</span> <span style="color: #f92672;">in</span> <span style="color: #f8f8f2;">strategies.items():</span></div>
<div><span style="color: #f8f8f2;">    model.fit(X_train_iris_scaled, y_train_iris)</span></div>
<div><span style="color: #f8f8f2;">    y_pred_iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">model.predict(X_test_iris_scaled)</span></div>
<div><span style="color: #f8f8f2;">    accuracy_iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">accuracy_score(y_test_iris, y_pred_iris)</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"</span><span style="color: #e6db74;">{name:13s}</span><span style="color: #e6db74;"> | </span><span style="color: #e6db74;">{accuracy_iris:.3f}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>
                        </div>
                    </div>

                    <h4>⚖️ Handling Class Imbalance</h4>
                    <div style="background: #fff8e1; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Simulate imbalanced dataset</div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.utils</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">class_weight</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">imblearn.over_sampling</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">SMOTE</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">collections</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">Counter</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Create imbalanced dataset (keep only 10% of malignant cases)</div>
<div><span style="color: #f8f8f2;">malignant_indices</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">np.where(y_train</span> <span style="color: #f92672;">==</span> <span style="color: #ae81ff;">0</span><span style="color: #f8f8f2;">)[0]</span></div>
<div><span style="color: #f8f8f2;">benign_indices</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">np.where(y_train</span> <span style="color: #f92672;">==</span> <span style="color: #ae81ff;">1</span><span style="color: #f8f8f2;">)[0]</span></div>

<div style="color: #75715e;"># Keep only 10% of malignant cases</div>
<div><span style="color: #f8f8f2;">keep_malignant</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">np.random.choice(malignant_indices, size=</span><span style="color: #66d9ef;">int</span><span style="color: #f92672;">(</span><span style="color: #66d9ef;">len</span><span style="color: #f92672;">(</span><span style="color: #f8f8f2;">malignant_indices</span><span style="color: #f92672;">)</span> <span style="color: #f92672;">*</span> <span style="color: #ae81ffcd /Users/admin/Desktop/WebSite

# Restore the proper JENKINS_SETUP.md
cat > JENKINS_SETUP.md << 'EOF'
# Jenkins Setup Documentation

## Overview
This document outlines the Jenkins CI/CD pipeline setup for the Ali Zanganeh AIML Portfolio.

## Pipeline Configuration
- **Pipeline Name**: website-portfolio-deployment
- **Trigger**: GitHub webhook on push to main branch
- **Agent**: macOS agent (macos-agent)
- **Deployment Target**: srv637-files.hstgr.io

## Deployment Process
1. Code checkout from GitHub repository
2. File validation and preprocessing
3. FTP deployment via lftp to hosting server
4. Deployment verification and status reporting

## Server Details
- **FTP Server**: srv637-files.hstgr.io
- **Target Directory**: /domains/zanganehai.com/public_html/
- **Protocol**: FTP with lftp client

## Status
✅ Jenkins pipeline operational and working
✅ Dual deployment with GitHub Actions
✅ Auto-deployment on code changes

## Recent Deployments
- Enhanced Chapter 1: ML Introduction with comprehensive Python examples
- Enhanced Chapter 2: Regression Analysis with complete implementations
- Enhanced Chapter 3: Classification Algorithms with hands-on coding

## Course Structure
Complete ML Fundamentals course with world-class content and executable Python code examples.
EOF

# Now add comprehensive Python code examples to Chapter 3
cat >> tutorials/ml-fundamentals/chapter3.html << 'EOF'

                <h2>💻 Hands-On Python Implementation</h2>
                <div class="azbn-card">
                    <h3>Classification Projects: From Theory to Practice</h3>
                    
                    <div style="background: #e8f5e8; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        <h4>📊 Binary Classification: Breast Cancer Detection</h4>
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Import essential libraries</div>
<div><span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">numpy</span> <span style="color: #f92672;">as</span> <span style="color: #f8f8f2;">np</span></div>
<div><span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">pandas</span> <span style="color: #f92672;">as</span> <span style="color: #f8f8f2;">pd</span></div>
<div><span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">matplotlib.pyplot</span> <span style="color: #f92672;">as</span> <span style="color: #f8f8f2;">plt</span></div>
<div><span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">seaborn</span> <span style="color: #f92672;">as</span> <span style="color: #f8f8f2;">sns</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.datasets</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">load_breast_cancer</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.model_selection</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">train_test_split, GridSearchCV, cross_val_score</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.preprocessing</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">StandardScaler</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.linear_model</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">LogisticRegression</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.svm</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">SVC</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.metrics</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">accuracy_score, classification_report, confusion_matrix</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.metrics</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">roc_curve, auc, precision_recall_curve</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Load the breast cancer dataset</div>
<div><span style="color: #f8f8f2;">cancer</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">load_breast_cancer()</span></div>
<div><span style="color: #f8f8f2;">df</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">pd.DataFrame(cancer.data, columns=cancer.feature_names)</span></div>
<div><span style="color: #f8f8f2;">df</span><span style="color: #f92672;">[</span><span style="color: #e6db74;">'target'</span><span style="color: #f92672;">]</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">cancer.target</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"Breast Cancer Dataset:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Shape: </span><span style="color: #e6db74;">{df.shape}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Features: </span><span style="color: #e6db74;">{len(cancer.feature_names)}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Classes: </span><span style="color: #e6db74;">{cancer.target_names}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Check class distribution</div>
<div><span style="color: #f8f8f2;">class_counts</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">df</span><span style="color: #f92672;">[</span><span style="color: #e6db74;">'target'</span><span style="color: #f92672;">]</span><span style="color: #f8f8f2;">.value_counts()</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"\nClass Distribution:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Malignant (0): </span><span style="color: #e6db74;">{class_counts[0]}</span><span style="color: #e6db74;"> ({class_counts[0]/len(df)*100:.1f}%)"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Benign (1): </span><span style="color: #e6db74;">{class_counts[1]}</span><span style="color: #e6db74;"> ({class_counts[1]/len(df)*100:.1f}%)"</span><span style="color: #f92672;">)</span></div>
                        </div>

                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Data exploration and visualization</div>
<div><span style="color: #f8f8f2;">plt.figure(figsize=(15, 5))</span></div>

<div style="color: #75715e;"># Class distribution</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 1)</span></div>
<div><span style="color: #f8f8f2;">class_counts.plot(kind=</span><span style="color: #e6db74;">'bar'</span><span style="color: #f8f8f2;">, color=[</span><span style="color: #e6db74;">'lightcoral'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'lightblue'</span><span style="color: #f8f8f2;">])</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Class Distribution'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'Class'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.ylabel(</span><span style="color: #e6db74;">'Count'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.xticks([0, 1], [</span><span style="color: #e6db74;">'Malignant'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'Benign'</span><span style="color: #f8f8f2;">], rotation=0)</span></div>

<div style="color: #75715e;"># Feature correlation heatmap (top 10 features)</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 2)</span></div>
<div><span style="color: #f8f8f2;">top_features</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">df.corr()[</span><span style="color: #e6db74;">'target'</span><span style="color: #f8f8f2;">].abs().nlargest(11).index[1:11]</span></div>
<div><span style="color: #f8f8f2;">corr_matrix</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">df[top_features].corr()</span></div>
<div><span style="color: #f8f8f2;">sns.heatmap(corr_matrix, annot=</span><span style="color: #ae81ff;">False</span><span style="color: #f8f8f2;">, cmap=</span><span style="color: #e6db74;">'coolwarm'</span><span style="color: #f8f8f2;">, center=0)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Top 10 Features Correlation'</span><span style="color: #f8f8f2;">)</span></div>

<div style="color: #75715e;"># Feature importance by correlation with target</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 3)</span></div>
<div><span style="color: #f8f8f2;">feature_corr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">df.corr()[</span><span style="color: #e6db74;">'target'</span><span style="color: #f8f8f2;">].abs().sort_values(ascending=</span><span style="color: #ae81ff;">False</span><span style="color: #f8f8f2;">)[1:11]</span></div>
<div><span style="color: #f8f8f2;">feature_corr.plot(kind=</span><span style="color: #e6db74;">'barh'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Top 10 Features by Target Correlation'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'Absolute Correlation'</span><span style="color: #f8f8f2;">)</span></div>

<div><span style="color: #f8f8f2;">plt.tight_layout()</span></div>
<div><span style="color: #f8f8f2;">plt.show()</span></div>
                        </div>
                    </div>

                    <h4>📈 Logistic Regression Implementation</h4>
                    <div style="background: #e3f2fd; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Prepare data for modeling</div>
<div><span style="color: #f8f8f2;">X</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">cancer.data</span></div>
<div><span style="color: #f8f8f2;">y</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">cancer.target</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Train-test split</div>
<div><span style="color: #f8f8f2;">X_train, X_test, y_train, y_test</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">train_test_split(</span></div>
<div><span style="color: #f8f8f2;">    X, y, test_size=0.2, random_state=42, stratify=y</span></div>
<div><span style="color: #f8f8f2;">)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Training set: </span><span style="color: #e6db74;">{X_train.shape[0]}</span><span style="color: #e6db74;"> samples"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Test set: </span><span style="color: #e6db74;">{X_test.shape[0]}</span><span style="color: #e6db74;"> samples"</span><span style="color: #f92672;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Feature scaling (important for logistic regression)</div>
<div><span style="color: #f8f8f2;">scaler</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">StandardScaler()</span></div>
<div><span style="color: #f8f8f2;">X_train_scaled</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">scaler.fit_transform(X_train)</span></div>
<div><span style="color: #f8f8f2;">X_test_scaled</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">scaler.transform(X_test)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Train logistic regression</div>
<div><span style="color: #f8f8f2;">lr_model</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">LogisticRegression(random_state=42, max_iter=1000)</span></div>
<div><span style="color: #f8f8f2;">lr_model.fit(X_train_scaled, y_train)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Make predictions</div>
<div><span style="color: #f8f8f2;">y_pred_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">lr_model.predict(X_test_scaled)</span></div>
<div><span style="color: #f8f8f2;">y_pred_proba_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">lr_model.predict_proba(X_test_scaled)[:, 1]</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Evaluate performance</div>
<div><span style="color: #f8f8f2;">accuracy_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">accuracy_score(y_test, y_pred_lr)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"\nLogistic Regression Results:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Accuracy: </span><span style="color: #e6db74;">{accuracy_lr:.3f}</span><span style="color: #e6db74;"> (</span><span style="color: #e6db74;">{accuracy_lr*100:.1f}</span><span style="color: #e6db74;">%)"</span><span style="color: #f92672;">)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"\nDetailed Classification Report:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #f8f8f2;">classification_report(y_test, y_pred_lr, target_names=cancer.target_names)</span><span style="color: #f92672;">)</span></div>
                        </div>

                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Analyze coefficients (feature importance)</div>
<div><span style="color: #f8f8f2;">feature_importance_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">pd.DataFrame({</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'feature'</span><span style="color: #f8f8f2;">: cancer.feature_names,</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'coefficient'</span><span style="color: #f8f8f2;">: lr_model.coef_[0],</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'abs_coefficient'</span><span style="color: #f8f8f2;">: np.abs(lr_model.coef_[0])</span></div>
<div><span style="color: #f8f8f2;">}).sort_values(</span><span style="color: #e6db74;">'abs_coefficient'</span><span style="color: #f8f8f2;">, ascending=</span><span style="color: #ae81ff;">False</span><span style="color: #f8f8f2;">)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"\nTop 10 Most Important Features:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #f8f8f2;">feature_importance_lr.head(10)</span><span style="color: #f92672;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Visualization of top features</div>
<div><span style="color: #f8f8f2;">plt.figure(figsize=(10, 6))</span></div>
<div><span style="color: #f8f8f2;">top_10_features</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">feature_importance_lr.head(10)</span></div>
<div><span style="color: #f8f8f2;">plt.barh(</span><span style="color: #66d9ef;">range</span><span style="color: #f92672;">(</span><span style="color: #ae81ff;">10</span><span style="color: #f92672;">)</span><span style="color: #f8f8f2;">, top_10_features[</span><span style="color: #e6db74;">'coefficient'</span><span style="color: #f8f8f2;">])</span></div>
<div><span style="color: #f8f8f2;">plt.yticks(</span><span style="color: #66d9ef;">range</span><span style="color: #f92672;">(</span><span style="color: #ae81ff;">10</span><span style="color: #f92672;">)</span><span style="color: #f8f8f2;">, top_10_features[</span><span style="color: #e6db74;">'feature'</span><span style="color: #f8f8f2;">])</span></div>
<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'Coefficient Value'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Top 10 Feature Coefficients in Logistic Regression'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.axvline(x=0, color=</span><span style="color: #e6db74;">'red'</span><span style="color: #f8f8f2;">, linestyle=</span><span style="color: #e6db74;">'--'</span><span style="color: #f8f8f2;">, alpha=0.7)</span></div>
<div><span style="color: #f8f8f2;">plt.tight_layout()</span></div>
<div><span style="color: #f8f8f2;">plt.show()</span></div>
                        </div>
                    </div>

                    <h4>⚡ Support Vector Machine Implementation</h4>
                    <div style="background: #fff8e1; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># SVM with different kernels</div>
<div><span style="color: #f8f8f2;">kernels</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">[</span><span style="color: #e6db74;">'linear'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'rbf'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'poly'</span><span style="color: #f8f8f2;">]</span></div>
<div><span style="color: #f8f8f2;">svm_results</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">{}</span></div>

<div><span style="color: #f92672;">for</span> <span style="color: #f8f8f2;">kernel</span> <span style="color: #f92672;">in</span> <span style="color: #f8f8f2;">kernels:</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #75715e;"># Train SVM with different kernel</span></div>
<div><span style="color: #f8f8f2;">    svm_model</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">SVC(kernel=kernel, random_state=42, probability=</span><span style="color: #ae81ff;">True</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">    svm_model.fit(X_train_scaled, y_train)</span></div>
    
<div><span style="color: #f8f8f2;">    </span><span style="color: #75715e;"># Predictions</span></div>
<div><span style="color: #f8f8f2;">    y_pred_svm</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">svm_model.predict(X_test_scaled)</span></div>
<div><span style="color: #f8f8f2;">    y_pred_proba_svm</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">svm_model.predict_proba(X_test_scaled)[:, 1]</span></div>
    
<div><span style="color: #f8f8f2;">    </span><span style="color: #75715e;"># Store results</span></div>
<div><span style="color: #f8f8f2;">    accuracy_svm</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">accuracy_score(y_test, y_pred_svm)</span></div>
<div><span style="color: #f8f8f2;">    svm_results[kernel]</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">{</span></div>
<div><span style="color: #f8f8f2;">        </span><span style="color: #e6db74;">'model'</span><span style="color: #f8f8f2;">: svm_model,</span></div>
<div><span style="color: #f8f8f2;">        </span><span style="color: #e6db74;">'accuracy'</span><span style="color: #f8f8f2;">: accuracy_svm,</span></div>
<div><span style="color: #f8f8f2;">        </span><span style="color: #e6db74;">'predictions'</span><span style="color: #f8f8f2;">: y_pred_svm,</span></div>
<div><span style="color: #f8f8f2;">        </span><span style="color: #e6db74;">'probabilities'</span><span style="color: #f8f8f2;">: y_pred_proba_svm</span></div>
<div><span style="color: #f8f8f2;">    }</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Display SVM results</div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"SVM Results with Different Kernels:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"Kernel   | Accuracy"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"-" * 18</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #f92672;">for</span> <span style="color: #f8f8f2;">kernel, results</span> <span style="color: #f92672;">in</span> <span style="color: #f8f8f2;">svm_results.items():</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"</span><span style="color: #e6db74;">{kernel:8s}</span><span style="color: #e6db74;"> | </span><span style="color: #e6db74;">{results['accuracy']:.3f}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Best SVM model</div>
<div><span style="color: #f8f8f2;">best_kernel</span> <span style="color: #f92672;">=</span> <span style="color: #66d9ef;">max</span><span style="color: #f92672;">(</span><span style="color: #f8f8f2;">svm_results, key=</span><span style="color: #f92672;">lambda</span> <span style="color: #f8f8f2;">k: svm_results[k][</span><span style="color: #e6db74;">'accuracy'</span><span style="color: #f8f8f2;">])</span></div>
<div><span style="color: #f8f8f2;">best_svm</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">svm_results[best_kernel]</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"\nBest SVM kernel: </span><span style="color: #e6db74;">{best_kernel}</span><span style="color: #e6db74;"> (Accuracy: </span><span style="color: #e6db74;">{best_svm['accuracy']:.3f}</span><span style="color: #e6db74;">)"</span><span style="color: #f92672;">)</span></div>
                        </div>
                    </div>

                    <h4>🔍 Hyperparameter Tuning with GridSearchCV</h4>
                    <div style="background: #f3e5f5; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># GridSearch for SVM hyperparameters</div>
<div><span style="color: #f8f8f2;">param_grid</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">{</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'C'</span><span style="color: #f8f8f2;">: [0.1, 1, 10, 100],</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'gamma'</span><span style="color: #f8f8f2;">: [</span><span style="color: #e6db74;">'scale'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'auto'</span><span style="color: #f8f8f2;">, 0.001, 0.01, 0.1, 1],</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'kernel'</span><span style="color: #f8f8f2;">: [</span><span style="color: #e6db74;">'rbf'</span><span style="color: #f8f8f2;">, </span><span style="color: #e6db74;">'poly'</span><span style="color: #f8f8f2;">]</span></div>
<div><span style="color: #f8f8f2;">}</span></div>

<div><span style="color: #f8f8f2;">svm_grid</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">GridSearchCV(</span></div>
<div><span style="color: #f8f8f2;">    SVC(random_state=42, probability=</span><span style="color: #ae81ff;">True</span><span style="color: #f8f8f2;">),</span></div>
<div><span style="color: #f8f8f2;">    param_grid,</span></div>
<div><span style="color: #f8f8f2;">    cv=5,</span></div>
<div><span style="color: #f8f8f2;">    scoring=</span><span style="color: #e6db74;">'accuracy'</span><span style="color: #f8f8f2;">,</span></div>
<div><span style="color: #f8f8f2;">    n_jobs=-1,</span></div>
<div><span style="color: #f8f8f2;">    verbose=1</span></div>
<div><span style="color: #f8f8f2;">)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"Starting GridSearch for SVM hyperparameters..."</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #f8f8f2;">svm_grid.fit(X_train_scaled, y_train)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"\nBest parameters: </span><span style="color: #e6db74;">{svm_grid.best_params_}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"Best cross-validation score: </span><span style="color: #e6db74;">{svm_grid.best_score_:.3f}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Evaluate optimized model</div>
<div><span style="color: #f8f8f2;">best_svm_optimized</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">svm_grid.best_estimator_</span></div>
<div><span style="color: #f8f8f2;">y_pred_optimized</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">best_svm_optimized.predict(X_test_scaled)</span></div>
<div><span style="color: #f8f8f2;">accuracy_optimized</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">accuracy_score(y_test, y_pred_optimized)</span></div>

<div style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"\nOptimized SVM Test Accuracy: </span><span style="color: #e6db74;">{accuracy_optimized:.3f}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>
                        </div>
                    </div>

                    <h4>📊 Comprehensive Model Evaluation</h4>
                    <div style="background: #e8f5e8; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Confusion Matrix</div>
<div><span style="color: #f8f8f2;">plt.figure(figsize=(15, 5))</span></div>

<div style="color: #75715e;"># Logistic Regression Confusion Matrix</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 1)</span></div>
<div><span style="color: #f8f8f2;">cm_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">confusion_matrix(y_test, y_pred_lr)</span></div>
<div><span style="color: #f8f8f2;">sns.heatmap(cm_lr, annot=</span><span style="color: #ae81ff;">True</span><span style="color: #f8f8f2;">, fmt=</span><span style="color: #e6db74;">'d'</span><span style="color: #f8f8f2;">, cmap=</span><span style="color: #e6db74;">'Blues'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Logistic Regression\nConfusion Matrix'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'Predicted'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.ylabel(</span><span style="color: #e6db74;">'Actual'</span><span style="color: #f8f8f2;">)</span></div>

<div style="color: #75715e;"># ROC Curves</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 2)</span></div>

<div style="color: #75715e;"># Logistic Regression ROC</div>
<div><span style="color: #f8f8f2;">fpr_lr, tpr_lr, _</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">roc_curve(y_test, y_pred_proba_lr)</span></div>
<div><span style="color: #f8f8f2;">auc_lr</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">auc(fpr_lr, tpr_lr)</span></div>
<div><span style="color: #f8f8f2;">plt.plot(fpr_lr, tpr_lr, label=</span><span style="color: #e6db74;">f'Logistic Regression (AUC = </span><span style="color: #e6db74;">{auc_lr:.3f}</span><span style="color: #e6db74;">)'</span><span style="color: #f8f8f2;">)</span></div>

<div style="color: #75715e;"># SVM ROC</div>
<div><span style="color: #f8f8f2;">y_pred_proba_svm_opt</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">best_svm_optimized.predict_proba(X_test_scaled)[:, 1]</span></div>
<div><span style="color: #f8f8f2;">fpr_svm, tpr_svm, _</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">roc_curve(y_test, y_pred_proba_svm_opt)</span></div>
<div><span style="color: #f8f8f2;">auc_svm</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">auc(fpr_svm, tpr_svm)</span></div>
<div><span style="color: #f8f8f2;">plt.plot(fpr_svm, tpr_svm, label=</span><span style="color: #e6db74;">f'SVM (AUC = </span><span style="color: #e6db74;">{auc_svm:.3f}</span><span style="color: #e6db74;">)'</span><span style="color: #f8f8f2;">)</span></div>

<div><span style="color: #f8f8f2;">plt.plot([0, 1], [0, 1], </span><span style="color: #e6db74;">'k--'</span><span style="color: #f8f8f2;">, label=</span><span style="color: #e6db74;">'Random Classifier'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'False Positive Rate'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.ylabel(</span><span style="color: #e6db74;">'True Positive Rate'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'ROC Curve Comparison'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.legend()</span></div>

<div style="color: #75715e;"># Precision-Recall Curves</div>
<div><span style="color: #f8f8f2;">plt.subplot(1, 3, 3)</span></div>

<div><span style="color: #75715e;"># Logistic Regression PR Curve</div>
<div><span style="color: #f8f8f2;">precision_lr, recall_lr, _</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">precision_recall_curve(y_test, y_pred_proba_lr)</span></div>
<div><span style="color: #f8f8f2;">plt.plot(recall_lr, precision_lr, label=</span><span style="color: #e6db74;">'Logistic Regression'</span><span style="color: #f8f8f2;">)</span></div>

<div style="color: #75715e;"># SVM PR Curve</div>
<div><span style="color: #f8f8f2;">precision_svm, recall_svm, _</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">precision_recall_curve(y_test, y_pred_proba_svm_opt)</span></div>
<div><span style="color: #f8f8f2;">plt.plot(recall_svm, precision_svm, label=</span><span style="color: #e6db74;">'SVM'</span><span style="color: #f8f8f2;">)</span></div>

<div><span style="color: #f8f8f2;">plt.xlabel(</span><span style="color: #e6db74;">'Recall'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.ylabel(</span><span style="color: #e6db74;">'Precision'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.title(</span><span style="color: #e6db74;">'Precision-Recall Curve'</span><span style="color: #f8f8f2;">)</span></div>
<div><span style="color: #f8f8f2;">plt.legend()</span></div>

<div><span style="color: #f8f8f2;">plt.tight_layout()</span></div>
<div><span style="color: #f8f8f2;">plt.show()</span></div>
                        </div>
                    </div>

                    <h4>🌍 Multi-Class Classification Example</h4>
                    <div style="background: #e3f2fd; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Multi-class classification with Iris dataset</div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.datasets</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">load_iris</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.multiclass</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">OneVsRestClassifier, OneVsOneClassifier</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Load Iris dataset</div>
<div><span style="color: #f8f8f2;">iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">load_iris()</span></div>
<div><span style="color: #f8f8f2;">X_iris, y_iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">iris.data, iris.target</span></div>

<div><span style="color: #f8f8f2;">X_train_iris, X_test_iris, y_train_iris, y_test_iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">train_test_split(</span></div>
<div><span style="color: #f8f8f2;">    X_iris, y_iris, test_size=0.3, random_state=42, stratify=y_iris</span></div>
<div><span style="color: #f8f8f2;">)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Scale features</div>
<div><span style="color: #f8f8f2;">scaler_iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">StandardScaler()</span></div>
<div><span style="color: #f8f8f2;">X_train_iris_scaled</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">scaler_iris.fit_transform(X_train_iris)</span></div>
<div><span style="color: #f8f8f2;">X_test_iris_scaled</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">scaler_iris.transform(X_test_iris)</span></div>

<div style="color: #75715e; margin-top: 1rem;"># Compare different multi-class strategies</div>
<div><span style="color: #f8f8f2;">strategies</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">{</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'Native'</span><span style="color: #f8f8f2;">: LogisticRegression(random_state=42, max_iter=1000),</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'One-vs-Rest'</span><span style="color: #f8f8f2;">: OneVsRestClassifier(SVC(kernel=</span><span style="color: #e6db74;">'rbf'</span><span style="color: #f8f8f2;">, random_state=42)),</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #e6db74;">'One-vs-One'</span><span style="color: #f8f8f2;">: OneVsOneClassifier(SVC(kernel=</span><span style="color: #e6db74;">'rbf'</span><span style="color: #f8f8f2;">, random_state=42))</span></div>
<div><span style="color: #f8f8f2;">}</span></div>

<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"Multi-class Classification Results:"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"Strategy      | Accuracy"</span><span style="color: #f92672;">)</span></div>
<div><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">"-" * 22</span><span style="color: #f92672;">)</span></div>

<div><span style="color: #f92672;">for</span> <span style="color: #f8f8f2;">name, model</span> <span style="color: #f92672;">in</span> <span style="color: #f8f8f2;">strategies.items():</span></div>
<div><span style="color: #f8f8f2;">    model.fit(X_train_iris_scaled, y_train_iris)</span></div>
<div><span style="color: #f8f8f2;">    y_pred_iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">model.predict(X_test_iris_scaled)</span></div>
<div><span style="color: #f8f8f2;">    accuracy_iris</span> <span style="color: #f92672;">=</span> <span style="color: #f8f8f2;">accuracy_score(y_test_iris, y_pred_iris)</span></div>
<div><span style="color: #f8f8f2;">    </span><span style="color: #66d9ef;">print</span><span style="color: #f92672;">(</span><span style="color: #e6db74;">f"</span><span style="color: #e6db74;">{name:13s}</span><span style="color: #e6db74;"> | </span><span style="color: #e6db74;">{accuracy_iris:.3f}</span><span style="color: #e6db74;">"</span><span style="color: #f92672;">)</span></div>
                        </div>
                    </div>

                    <h4>⚖️ Handling Class Imbalance</h4>
                    <div style="background: #fff8e1; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                        
                        <div style="background: #1e1e1e; color: #f8f8f2; padding: 1rem; border-radius: 6px; margin: 1rem 0; font-family: 'Courier New', monospace; font-size: 0.9rem;">
<div style="color: #75715e;"># Simulate imbalanced dataset</div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">sklearn.utils</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">class_weight</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">imblearn.over_sampling</span> <span style="color: #f92672;">import</span> <span style="color: #f8f8f2;">SMOTE</span></div>
<div><span style="color: #f92672;">from</span> <span style="color: #f8f8f2;">collections</span> <span style=# Jenkins Setup Documentation

## Overview
This document outlines the Jenkins CI/CD pipeline setup for the Ali Zanganeh AIML Portfolio.

## Pipeline Configuration
- **Pipeline Name**: website-portfolio-deployment
- **Trigger**: GitHub webhook on push to main branch
- **Agent**: macOS agent (macos-agent)
- **Deployment Target**: srv637-files.hstgr.io

## Deployment Process
1. Code checkout from GitHub repository
2. File validation and preprocessing
3. FTP deployment via lftp to hosting server
4. Deployment verification and status reporting

## Server Details
- **FTP Server**: srv637-files.hstgr.io
- **Target Directory**: /domains/zanganehai.com/public_html/
- **Protocol**: FTP with lftp client

## Status
✅ Jenkins pipeline operational and working
✅ Dual deployment with GitHub Actions
✅ Auto-deployment on code changes
