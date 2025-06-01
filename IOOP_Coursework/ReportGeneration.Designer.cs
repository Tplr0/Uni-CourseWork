namespace assignment
{
    partial class ReportGeneration
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.comboBox2 = new System.Windows.Forms.ComboBox();
            this.btnGenerateServiceReport = new System.Windows.Forms.Button();
            this.btnGenerateCustomerReport = new System.Windows.Forms.Button();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Location = new System.Drawing.Point(89, 28);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(121, 24);
            this.comboBox1.TabIndex = 0;
            // 
            // comboBox2
            // 
            this.comboBox2.FormattingEnabled = true;
            this.comboBox2.Location = new System.Drawing.Point(89, 104);
            this.comboBox2.Name = "comboBox2";
            this.comboBox2.Size = new System.Drawing.Size(121, 24);
            this.comboBox2.TabIndex = 1;
            // 
            // btnGenerateServiceReport
            // 
            this.btnGenerateServiceReport.Location = new System.Drawing.Point(366, 28);
            this.btnGenerateServiceReport.Name = "btnGenerateServiceReport";
            this.btnGenerateServiceReport.Size = new System.Drawing.Size(250, 53);
            this.btnGenerateServiceReport.TabIndex = 2;
            this.btnGenerateServiceReport.Text = "Service report";
            this.btnGenerateServiceReport.UseVisualStyleBackColor = true;
            this.btnGenerateServiceReport.Click += new System.EventHandler(this.button1_Click);
            // 
            // btnGenerateCustomerReport
            // 
            this.btnGenerateCustomerReport.Location = new System.Drawing.Point(366, 104);
            this.btnGenerateCustomerReport.Name = "btnGenerateCustomerReport";
            this.btnGenerateCustomerReport.Size = new System.Drawing.Size(250, 53);
            this.btnGenerateCustomerReport.TabIndex = 3;
            this.btnGenerateCustomerReport.Text = "Customer report";
            this.btnGenerateCustomerReport.UseVisualStyleBackColor = true;
            this.btnGenerateCustomerReport.Click += new System.EventHandler(this.button2_Click);
            // 
            // dataGridView1
            // 
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(89, 198);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowHeadersWidth = 51;
            this.dataGridView1.RowTemplate.Height = 24;
            this.dataGridView1.Size = new System.Drawing.Size(527, 198);
            this.dataGridView1.TabIndex = 4;
            // 
            // ReportGeneration
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.btnGenerateCustomerReport);
            this.Controls.Add(this.btnGenerateServiceReport);
            this.Controls.Add(this.comboBox2);
            this.Controls.Add(this.comboBox1);
            this.Name = "ReportGeneration";
            this.Text = "Report Generation";
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.ComboBox comboBox2;
        private System.Windows.Forms.Button btnGenerateServiceReport;
        private System.Windows.Forms.Button btnGenerateCustomerReport;
        private System.Windows.Forms.DataGridView dataGridView1;
    }
}