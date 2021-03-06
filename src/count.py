from extract_all_tags import * 


if __name__ == "__main__":
    zip_content = pd.read_csv(os.path.join(repo_dir, content_fn))
    states = zip_content.loc[zip_content["type"]=="states"] 

    file_counts = {}
    fullCaseName_counts = {}
    for zip_file in get_all_state_zips(): 
        num = zip_file[:-4]
        try:
            with open(f"../tags/{num}_tags.json") as injson:
                curr_fullCaseName = 0
                curr_tags = json.load(injson)
                file_counts[zip_file] = len(curr_tags) 
                for fn, tags in curr_tags.items():
                    curr_fullCaseName += tags.get("fullCaseName",0)
                fullCaseName_counts[zip_file] = curr_fullCaseName
        except FileNotFoundError:
            pass

    states["file_count"] = states["zip"].map(file_counts)
    states["fullCaseName_count"] = states["zip"].map(fullCaseName_counts)

    states.to_csv(os.path.join(repo_dir,"state_counts.csv"),index=False)
