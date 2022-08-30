import pandas as pd
from urllib.request import Request, urlopen
import os
from datetime import datetime

def combine_csv_files(filenames):
    """ Takes an array of filenames (csv files) and combines
        into one array

    Args:
        filenames (array): array of filenames
    """
    export_df = pd.DataFrame()
    for file in filenames:
        temp_df = pd.read_csv(file, encoding="latin-1").fillna("")

        if export_df.empty == True:
            export_df = temp_df
        else:
            export_df = pd.concat([export_df,temp_df])

        
def download_file_from_url(url, outputFilePath, outputFileName):
    """ Downloads file from URL and saves it to folder under set filename

    Args:
        url (str): url of file to download
        outputFilePath (str): Folder to save in
        outputFileName(str): Filename to save as
    """
    try:
        req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
        response = urlopen(req, timeout=20)
        file = open(os.getcwd() + outputFilePath + "/" + outputFileName,"wb")
        file.write(response.read())
        file.close()
        return True
    except:
        print("Could not download file from: " + str(url))
        return False
    
   
from fpdf import FPDF 
def create_fpdf_pdf(pdfTitle, orientation, fonts):
    """_summary_

    Args:
        pdfTitle (str): Title of PDF
        orientation (str): L or P
        fonts (array): 2D array with font (ttf) name and path
    """
    pdf = FPDF(orientation, 'mm', 'A4')
    pdf.set_title('BlackBee Economic Indicators')
    
    for font in fonts:
        pdf.add_font(font[0], '', font[1], uni=True)
    
    return pdf


from PyPDF2 import PdfFileMerger, PdfFileReader
def merge_pdfs(arrayOfPDFs, outputFilePath, outputFileName):
    """ Mergers multiple PDFs into one

    Args:
        arrayOfPDFs (array): array of pdf filepaths
        outputFilePath (str): Folder to save in
        outputFileName (str): Filename to save as
    """
    
    merger = PdfFileMerger()
    
    for file in arrayOfPDFs:
         merger.append(PdfFileReader(open(file, 'rb')))
         
    merger.write(outputFilePath + "/" + outputFileName + ".pdf")
    

def add_line_chart_to_workbook(workbook, worksheet, SOURCE, CHART_TITLE, EXCEL_SHEET_NAME,EXCEL_INDEX_COL,EXCEL_VALUES_COL, EXCEL_CHART_LOCATION, length_of_df, xlabel = None, ylabel = None):
    """This function adds a line chart to the Excel Workbook
    Args:
        workbook ([type]): Workbook Object
        worksheet ([type]): Worksheet Object
        SOURCE ([type]): Source of data (e.g. CSO, Daft etc..)
        CHART_TITLE ([type]): The title for the chart
        EXCEL_SHEET_NAME ([type]): Sheet name (<32 characters)
        EXCEL_INDEX_COL ([type]): The column in numerical form in for the x-axis (To chart with x axis values from Col A = 0)
        EXCEL_VALUES_COL ([type]): An array which contains column positions to be charted. (To chart lines with values from Col B + C = [1,2])
        length_of_df ([type]): The number of rows to chart
    """

    chart = workbook.add_chart({'type': 'line'})
    chart.set_title({ 'name': SOURCE + ' | ' + CHART_TITLE})
    chart.set_x_axis({'name': xlabel, 'label_position':'low'})
    chart.set_size({'width': 850, 'height': 450})
    chart.set_y_axis({'name': ylabel,'major_gridlines': {'visible': False},})
    chart.set_legend({'position': 'bottom'})

    for valueCol in EXCEL_VALUES_COL:
        chart.add_series({
            'name': [EXCEL_SHEET_NAME, 0, valueCol],
            'categories': [EXCEL_SHEET_NAME, 1, EXCEL_INDEX_COL, length_of_df, EXCEL_INDEX_COL],
            'values': [EXCEL_SHEET_NAME, 1, valueCol, length_of_df, valueCol],
        })

    worksheet.insert_chart(EXCEL_CHART_LOCATION, chart)
    

def add_column_chart_to_workbook(workbook, worksheet, SOURCE, CHART_TITLE, EXCEL_SHEET_NAME,EXCEL_INDEX_COL,EXCEL_VALUES_COL, EXCEL_CHART_LOCATION, length_of_df):
    """This function adds a column chart to the Excel Workbook
    Args:
        workbook ([type]): Workbook Object
        worksheet ([type]): Worksheet Object
        SOURCE ([type]): Source of data (e.g. CSO, Daft etc..)
        CHART_TITLE ([type]): The title for the chart
        EXCEL_SHEET_NAME ([type]): Sheet name (<32 characters)
        EXCEL_INDEX_COL ([type]): The column in numerical form in for the x-axis (To chart with x axis values from Col A = 0)
        EXCEL_VALUES_COL ([type]): An array which contains column positions to be charted. (To chart lines with values from Col B + C = [1,2])
        length_of_df ([type]): The number of rows to chart
    """
    
    chart = workbook.add_chart({'type': 'column'})
    chart.set_title({ 'name': SOURCE + ' | ' + CHART_TITLE})
    chart.set_x_axis({'name': '', 'label_position':'low'})
    chart.set_size({'width': 850, 'height': 450})
    chart.set_y_axis({'name': '','major_gridlines': {'visible': False},})
    chart.set_legend({'position': 'bottom'})

    for valueCol in EXCEL_VALUES_COL:
        chart.add_series({
            'name': [EXCEL_SHEET_NAME, 0, valueCol],
            'categories': [EXCEL_SHEET_NAME, 1, EXCEL_INDEX_COL, length_of_df, EXCEL_INDEX_COL],
            'values': [EXCEL_SHEET_NAME, 1, valueCol, length_of_df, valueCol],
        })

    worksheet.insert_chart(EXCEL_CHART_LOCATION, chart)
    
def check_for_news(news_items_dict, df, latest_rel_url, SOURCE_NAME, FUNCTION_NAME):
    """ Pass in blog/news articles from any website and checks if there has been a recent addition

    Args:
        news_items_dict (_type_): dictionary of news articles
        df (_type_): df
        latest_rel_url (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        latest_news_peice_on_website = list(news_items_dict.keys())[0]
    
        # CONDITION 1. If we have no existing source in the CSV, append latest news piece and end.
        if df[df['Source'].str.contains(SOURCE_NAME + '-' + FUNCTION_NAME)].count()['Source'] == 0:
            df.loc[len(df)] = [SOURCE_NAME + '-' + FUNCTION_NAME, latest_news_peice_on_website, datetime.now().strftime("%d %B, %Y %H:%M")]
            df.to_csv(latest_rel_url, index=False)
            
            data = SOURCE_NAME + ' - ' + latest_news_peice_on_website + ', <a href="' + news_items_dict[latest_news_peice_on_website] + '">Go to link</a>'
            return data
        
        # CONDITION 2. Else if the source exists, check the latest artice we caught previously against the articles we caught now.
        else:
            # CONDITION 2.1 If there has been no new article released, then we can end.
            if df.loc[df['Source'] == SOURCE_NAME + '-' + FUNCTION_NAME]['Latest'].values[0] == latest_news_peice_on_website:
                data = ''
                return data
            
            #  CONDITION 2.2 There is new articles there, we need to check how many new articles have been released since.
            else:
                keys = list(news_items_dict.keys())
                
                # Make sure the article we have is in the list of articles from the website.
                if df.loc[df['Source'] == SOURCE_NAME + '-' + FUNCTION_NAME]['Latest'].values[0] in keys:
                    index = keys.index(df.loc[df['Source'] == SOURCE_NAME + '-' + FUNCTION_NAME]['Latest'].values[0])
                
                    # Selecting all article(s) that have been released since we last checked
                    data = []
                    for i in range(0,index):
                        data.append(SOURCE_NAME + ' - ' + keys[i] + ', <a href="' + news_items_dict[keys[i]] + '">Go to link</a>')
                   
                    # Update the CSV to the latest article on the website
                    df.loc[df['Source'] == SOURCE_NAME + '-' + FUNCTION_NAME, 'Latest'] = keys[0]
                    df.loc[df['Source'] == SOURCE_NAME + '-' + FUNCTION_NAME, 'Date'] = datetime.now().strftime("%d %B, %Y %H:%M")
                    df.to_csv(latest_rel_url, index=False)
            
                    data = '<br>'.join(data)
                    return data
                
                # If we cant find our latest one in the csv on the website, just return the latest one on the website
                else:
                  
                    # Update the CSV to the latest article on the website
                    df.loc[df['Source'] == SOURCE_NAME + '-' + FUNCTION_NAME, 'Latest'] = keys[0]
                    df.loc[df['Source'] == SOURCE_NAME + '-' + FUNCTION_NAME, 'Date'] = datetime.now().strftime("%d %B, %Y %H:%M")
                    df.to_csv(latest_rel_url, index=False)
                    
                    data = SOURCE_NAME + ' - ' + keys[0] + ', <a href="' + news_items_dict[keys[0]] + '">Go to link</a>'
                    return data
    except:
        data = 'Error: ' + SOURCE_NAME +' - ' + FUNCTION_NAME + ', Error in script. Please update.'
        return data
    
    
import itertools
def generate_combinations(n_products=21, step=5):
    """ Generates a list of combinations

    Args:
        n_products (int, optional): _description_. Defaults to 21.
        step (int, optional): _description_. Defaults to 5.

    Yields:
        _type_: _description_
    """
    array_of_nums = list(range(0, 100 + step, step))
    for combination in itertools.product(*[array_of_nums for x in range(n_products)]):
        if sum(combination) == 100:
            yield combination

for combo in itertools.islice(generate_combinations(), 10_000_000):
    print(combo)
    
    
# Alive Progress Example
from alive_progress import alive_bar

with alive_bar(1000) as bar:
    for i in compute():
        bar()