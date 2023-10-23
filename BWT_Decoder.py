def makeFirstColumn(bwt):    # Generate the first column of the Burrows-Wheeler Matrix
    return sorted(bwt)
    
def rank(bwt, row):         # Determine the rank of a character at a specific position
    char = bwt[row]
    return bwt[:row].count(char)

def applyLF(firstCol, char, rank):      # Apply the Last-First property
    return firstCol.index(char) + rank

def decodeBWT(bwt):
    firstCol = makeFirstColumn(bwt)
    text = ""
    row = 0
    while bwt[row] != '$':
        text += bwt[row]
        row = applyLF(firstCol, bwt[row], rank(bwt, row))
    return text[::-1]  # Reverse the text to get the original string

# String to decode
bwt_string = ".uspe_gexr_______$..,e.orrs,sdddeedkdsuoden-tf,tyewtktttt,sewteb_ce__ww__h_PPsm_u_naseueeennnrrlmwwhWcrskkmHwhttv_no_nnwttzKt_l_ocoo_be___aaaooaAakiiooett_oooi_sslllfyyD__uouuueceetenagan___rru_aasanIiatt__c__saacooor_ootjeae______ir__a"
decoded_string = decodeBWT(bwt_string)
print("Decoded string is:", decoded_string)

