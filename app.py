import streamlit as st
import re


def extract_id_from_url(url):
    # Define the regex pattern to match the id in the url
    pattern = r'id=([a-f0-9]+)'
    
    # Use the re.search function to find the id
    match = re.search(pattern, url)
    
    # If a match is found, return the id. Otherwise, return None.
    if match:
        return match.group(1)
    else:
        return None



# Define the main function for the Streamlit app
def main():
    
    st.title('IMCOM HTML Code Generator')

    # Add a text input for the user to enter their HTML code
    installation = st.text_input("Installation Name")
    installation_short = st.text_input("Installation Short Hand Name", help = "Can be found in the url of the Data and Apps page")

    st.write('#')
    
    master_plan_url = st.text_input("Master Plan Link")
    master_plan_id = extract_id_from_url(master_plan_url)

    st.write('#')

    airfield_url = st.text_input("Airfield Link")
    airfield_id = extract_id_from_url(airfield_url)
    airfield_image = st.text_input("Airfield Image URL")

    st.write('#')

    emer_serv_url = st.text_input("Emergency Services Link")
    emer_serv_id = extract_id_from_url(emer_serv_url)

    st.write('#')

    rec_fit_url = st.text_input("Rec & Fitness Link")
    rec_fit_id = extract_id_from_url(rec_fit_url)

    st.write('#')

    install_url = st.text_input("Installation Link")
    install_id = extract_id_from_url(install_url)
    install_image = st.text_input("Installation Image URL")

    st.write("#")

    grnd_maint_url = st.text_input("Ground Maintanence Link")
    grnd_maint_id = extract_id_from_url(grnd_maint_url)

    st.write("#")

    environ_url = st.text_input("Environmental Link")
    environ_id = extract_id_from_url(environ_url)

    st.write("#")




    # Add a button to generate the HTML code
    if st.button('Generate'):
        
        
        
        first_page = f"""

        <h2 class="text-center white-text" style="text-align: center;">{installation} Standardized Map Applications</h2>
        <div class="row">

        <!-- Add Application Cards Here DO NOT ADD BELOW THE   </div>-->

        <div class="col-xs-12 col-sm-6 col-md-3">
                <div class="calcite-web">
                        <div class="card-base">
                            <div class="card-image-wrap">
                                    <img class="”card-image”" src="https://aigp-iigg.obs.army.mil/portal/sharing/rest/content/items/9ecf0076b6eb4f4d8221e74dd87fa446/data" alt="Master Plan" style="width: 100%;" height="140px">
                            </div>
                            <div class="card-content" style="background-color:#22211f;">
                                <h4 style="text-align:left;font-size:19px;"><a target="_blank" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{master_plan_id}/about" class="yellow-text">
                                    Master Plan</a></h4>
                                <p style="min-height: 50px; margin-bottom: 10px;" class="white-text">
                                        The ExB app, called Master Plan, allows users to view various layers related to a specific theme. These layers 
                                        may include Planning, Real Property, Military Ranges and Training, and more.</p>
                            </div>
                            <div class="btn-group btn-group-justified" role="group">
                                    <a target="_blank" class="btn btn-default" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{master_plan_id}/about">
                                        Details</a>
                                    <a target="_blank" class="btn btn-primary" href="{master_plan_url}">
                                        View</a>
                                    </div>
                            </div>
                        </div>
                </div>
                
                
        <div class="col-xs-12 col-sm-6 col-md-3">
                <div class="calcite-web">
                        <div class="card-base">
                            <div class="card-image-wrap">
                                    <img class="”card-image”" src="{airfield_image}" alt="Airfield" style="width: 100%;" height="140px">
                            </div>
                            <div class="card-content" style="background-color:#22211f;">
                                <h4 style="text-align:left;font-size:19px;"><a target="_blank" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{airfield_id}/about" class="yellow-text">
                                    Airfield</a></h4>
                                <p style="min-height: 50px; margin-bottom: 10px;" class="white-text">
                                        The ExB app, called Airfield, allows users to view various layers related to a specific theme. These layers may include 
                                        CCF Transportation, Airfield, Military Ranges and Training, and more.</p>
                            </div>
                                <div class="btn-group btn-group-justified" role="group">
                                    <a target="_blank" class="btn btn-default" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{airfield_id}/about">
                                        Details</a>
                                    <a target="_blank" class="btn btn-primary" href="{airfield_url}">
                                        View</a>
                                    </div>
                            </div>
                        </div>
                    </div>
                    
                    
        <div class="col-xs-12 col-sm-6 col-md-3">
                <div class="calcite-web">
                        <div class="card-base">
                            <div class="card-image-wrap">
                                    <img class="”card-image”" src="https://aigp-iigg.obs.army.mil/portal/sharing/rest/content/items/6918d3710c39404db2035499258f290d/data" style="width: 100%;" alt="Emergency Services" height="140px">
                            </div>
                            <div class="card-content" style="background-color:#22211f;">
                                <h4 style="text-align:left;font-size:19px;"><a target="_blank" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{emer_serv_id}/about" class="yellow-text">
                                    Emergency Services</a></h4>
                                <p style="min-height: 50px; margin-bottom: 10px;" class="white-text">
                                        The ExB app, called Emergency Services, allows users to view various layers related to a specific theme. 
                                        These layers may include Emergency Services, Airfield, and more.</p>
                            </div>
                                <div class="btn-group btn-group-justified" role="group">
                                    <a target="_blank" class="btn btn-default" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{emer_serv_id}/about">
                                        Details</a>
                                    <a target="_blank" class="btn btn-primary" href="{emer_serv_url}">
                                        View</a>
                                    </div>
                            </div>
                        </div>
                    </div>
                    
                    
        <div class="col-xs-12 col-sm-6 col-md-3">
                <div class="calcite-web">
                        <div class="card-base">
                            <div class="card-image-wrap">
                                    <img class="”card-image”" src="https://aigp-iigg.obs.army.mil/portal/sharing/rest/content/items/383bd5ace18b40e98e018d3f7e47d2bd/data" style="width: 100%;" alt="Rec and Fitness" height="140px">
                            </div>
                            <div class="card-content" style="background-color:#22211f;">
                                <h4 style="text-align:left;font-size:19px;"><a target="_blank" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{rec_fit_id}/about" class="yellow-text">
                                    Recreation &amp; Fitness</a></h4>
                                <p style="min-height: 50px; margin-bottom: 10px;" class="white-text">
                                        The ExB app, called Fitness &amp; Recreation, allows users to view various layers related to a specific theme. These 
                                        layers may include Recreation, Real Property, and more.</p>
                            </div>
                                <div class="btn-group btn-group-justified" role="group">
                                    <a target="_blank" class="btn btn-default" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{rec_fit_id}/about">
                                        Details</a>
                                    <a target="_blank" class="btn btn-primary" href="{rec_fit_url}">
                                        View</a>
                                    </div>
                            </div>
                        </div>
                    </div>


        </div>

        """





        second_page = f"""

        <div class="col-xs-12 col-sm-6 col-md-3">
                <div class="calcite-web">
                        <div class="card-base">
                            <div class="card-image-wrap">
                                    <img class="”card-image”" src="{install_image}" alt="Installation" style="width: 100%;" height="140px">
                            </div>
                            <div class="card-content" style="background-color:#22211f;">
                                <h4 style="text-align:left;font-size:19px;"><a target="_blank" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{install_id}/about" class="yellow-text">
                                    Installation</a></h4>
                                <p style="min-height: 50px; margin-bottom: 10px;" class="white-text">
                                        The ExB app, called Installation, allows users to view various layers related to a specific theme. These layers may 
                                        include Real Property, Military Ranges and Training, Civil Works, and more.</p>
                            </div>
                                <div class="btn-group btn-group-justified" role="group">
                                    <a target="_blank" class="btn btn-default" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{install_id}/about">
                                        Details</a>
                                    <a target="_blank" class="btn btn-primary" href="{install_url}">
                                        View</a>
                                    </div>
                            </div>
                        </div>
                    </div>
                    
                    
        <div class="col-xs-12 col-sm-6 col-md-3">
                <div class="calcite-web">
                        <div class="card-base">
                            <div class="card-image-wrap">
                                    <img class="”card-image”" src="https://aigp-iigg.obs.army.mil/portal/sharing/rest/content/items/82a2a6d85b174992ae9520d5cdbcd45c/data" alt="Ground Maintenance" style="width: 100%;" height="140px">
                            </div>
                            <div class="card-content" style="background-color:#22211f;">
                                <h4 style="text-align:left;font-size:19px;"><a target="_blank" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{grnd_maint_id}/about" class="yellow-text">
                                    Ground Maintenance</a></h4>
                                <p style="min-height: 50px; margin-bottom: 10px;" class="white-text">
                                        The ExB app, called Grounds Maintenance, allows users to view various layers related to a specific theme. These layers 
                                        may include Civil Works, Clean Up , Cultural Resources, and more.</p>
                            </div>
                                <div class="btn-group btn-group-justified" role="group">
                                    <a target="_blank" class="btn btn-default" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{grnd_maint_id}/about">
                                        Details</a>
                                    <a target="_blank" class="btn btn-primary" href="{grnd_maint_url}">
                                        View</a>
                                    </div>
                            </div>
                        </div>
                    </div>
                    
                    
                    
        <div class="col-xs-12 col-sm-6 col-md-3">
                <div class="calcite-web">
                        <div class="card-base">
                            <div class="card-image-wrap">
                                    <img class="”card-image”" src="https://aigp-iigg.obs.army.mil/portal/sharing/rest/content/items/8b6ab30905064b0d8125f178c3dd6958/data" alt="Environmental" style="width: 100%;" height="140px">
                            </div>
                            <div class="card-content" style="background-color:#22211f;">
                                <h4 style="text-align:left;font-size:19px;"><a target="_blank" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{environ_id}/about" class="yellow-text">
                                    Environmental</a></h4>
                                <p style="min-height: 50px; margin-bottom: 10px;" class="white-text">
                                        The ExB app, called Environmental, allows users to view various layers related to a specific theme. These layers may 
                                        include Restricted Area, Cultural Resources, Compliance, and more.</p>
                            </div>
                                <div class="btn-group btn-group-justified" role="group">
                                    <a target="_blank" class="btn btn-default" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/apps/{environ_id}/about">
                                        Details</a>
                                    <a target="_blank" class="btn btn-primary" href="{environ_url}">
                                        View</a>
                                    </div>
                            </div>
                        </div>
                    </div>
                    
                    
                    
        <div class="col-xs-12">
            <p class="text-right white-text">
                    <a target="_blank" href="https://aigp-iigg.obs.army.mil/portal/apps/sites/#/{installation_short}/search? collection=App%2CMap" class="btn btn-primary">
                        Explore All Apps</a>
            </p>
        </div>

        """


      


        
        style_section = """
        
        <style>
            .white-text {
                color: white;
            }
            .yellow-text {
                color: #FEC325;
            }
        </style>

        """

                


        st.write('#')
        
        st.write("First Text Section HTML Code")

        st.code(first_page + style_section, language='html')


        st.write('#')
        
        st.write("Second Text Section HTML Code")

        st.code(second_page, language='html')

# Run the Streamlit app
if __name__ == "__main__":
    main()